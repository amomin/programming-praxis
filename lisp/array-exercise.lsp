;;; Array Exercise - May 8, 2018
;;;
;;; Given an array of distinct integers, replace each element of the array with
;;; its corresponding rank in the array. For instance, the input array
;;; [10,8,15,12,6,20,1] is replaced by the output array [4,3,6,5,2,7,1] because
;;; element 1 has rank 1, element 6 has rank 2, element 8 has rank 3, element
;;; 10 has rank 4, element 12 has rank 5, element 15 has rank 6, and element
;;; 20 has rank 7.

(defun binary-search-index (array-list item)
  (defun helper (array-list item left right)
    (let* ((mid (floor (/ (+ left right) 2)))
	   (lv (aref array-list left))
	   (rv (aref array-list right))
	   (mv (aref array-list mid))
	   )
      ;; So ugly, really should have thought through the loop invariants.
      ;; Hack for this exercise since this is auxilliary to the main goal below.
      (cond ((> lv item) nil)
	    ((< rv item) nil)
	    ((equal lv item) left)
	    ((equal rv item) right)
	    ((equal mv item) mid)
	    ((< mv item) (helper array-list item (+ mid 1) right))
	    ((> mv item) (helper array-list item left (- mid 1))))))
  (let ((left 0)
	(right (- (array-dimension array-list 0) 1)))
    (helper array-list item left right)))

(defun replace-by-rank (array-list)
  (let ((sorted (sort (copy-seq array-list) (function <))))
    (map '(vector)
	 (lambda (x) (binary-search-index sorted x))
	 array-list)))
