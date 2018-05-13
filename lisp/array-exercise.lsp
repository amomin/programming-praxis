;;; Array Exercise - May 8, 2018
;;;
;;; Given an array of distinct integers, replace each element of the array with
;;; its corresponding rank in the array. For instance, the input array
;;; [10,8,15,12,6,20,1] is replaced by the output array [4,3,6,5,2,7,1] because
;;; element 1 has rank 1, element 6 has rank 2, element 8 has rank 3, element
;;; 10 has rank 4, element 12 has rank 5, element 15 has rank 6, and element
;;; 20 has rank 7.

(defun binary-search-index (array-list item)
  "Binary search on a sorted array, implemented recursively (instead of
   iteratively) for simplicity.
   This function could be made more generic by passing in the comparison
   operator. Will leave this as a TODO."
  (defun helper (array-list item left right)
  " Invariants: left < right
               The value is in between left (inclusive) and right (exclusive)
                 if present at all.
   The invariants are preserved on each call of helper (unless they do not
   hold initially."
    (let* ((mid (floor (/ (+ left right) 2))))
      (cond ((>= left right) nil)
	    ; Not sure if this is the correct test for equality.
	    ((equal (aref array-list mid)  item) mid)
	    ((< (aref array-list mid) item) (helper array-list item (+ mid 1) right))
	    ((> (aref array-list mid) item) (helper array-list item left mid)))))
  (let ((left 0)
	(right (array-dimension array-list 0)))
    (helper array-list item left right)))

;; O(nlog(n)) solution - sort is nlog(n), and binary search is done
;; n times in O(log(n)) time and O(n) space.
;; Could make this generic by passing in the comparator instead of hardcoding
;; <.
(defun replace-by-rank (array-list)
  (let ((sorted (sort (copy-seq array-list) (function <))))
    (map '(vector)
	 (lambda (x) (binary-search-index sorted x))
	 array-list)))

(defun replace-by-rank-2 (array-list)
    "Second solution in a simpler, functional style.
     We take the array, replace elements int-val by
     (index int-val), sort by int-val, replace by (index sorted-index), sort by
     sorted-index and then map (index sorted-index) -> index to get back the
     original list with the value replaced by the index.
     No need for a binary search since the sort/indexing does all the work.
     Also O(nlogn) time and O(n) space, sorting twice."
  (labels ((indexify (alist)
	      (loop :for x :across alist
	            :for i :from 0
	            :collect (list i x)))
	   (replace-by-sorted-index (indexed-list)
	      (loop :for x :in indexed-list
	            :for i :from 0
		 ;:collect (list (first x) i)))
		 :collect (list i (first x))))
	   (compare-by-second (x y) (< (second x) (second y)))
	   (drop-value (plain-list)
	      (loop :for x :in plain-list
		 :collect (first x))))
    (drop-value
        (sort
	    (replace-by-sorted-index
	        (sort (indexify array-list) (function compare-by-second)))
	     (function compare-by-second)))))
