;;;; Searching an Infinite Array
;;;; December 9, 2016

;; Given a sorted infinite array, write a method that
;; finds an item in the list.  It should run in time O(log(index))
;; where `index` is the index of the item in the list (or the index
;; of the item in the position where it would be if it were in the
;; list).

;; I should have defined a data type / interface for handling
;; infinite lists.  In my defence, I don't know how data types
;; work in common lisp yet.  The following works for finite
;; lists of unkown length withouth refering to the length
;; function, and requires that list can be applied to the
;; subsequence function and the nth-element function.

(defun inf-search (list item)
  ;; Search an infinite (or finite of unknown length) list
  ;; in log time
  (defun inf-search-skip (l skip it)
    (let ((target (nth (- skip 1) l)))
      (cond
	((and (null target) (null l)) ;Empty list
	 nil)
	((and (null target) (> skip 1)) ;Not enough items in list
	 (inf-search-skip l (/ skip 2) it))
	((< target it) ; Searched item is too small, continue on remainder of list with larger skip
	 (inf-search-skip (subseq l skip) (* skip 2) it))
	((= target it) ; Found, return true
	 't)
	((and (> target it) (> skip 1)) ; Searched item is too large, halve the skip step
	 (inf-search-skip l (/ skip 2) it)) ;First item in list is too large, it's not in the list.  return nil.
	((> target it)
	 nil))))
  (inf-search-skip list 1 item))

(defun client-inf-search (n)
  ;; Demonstrates use of search on a list containing
  ;; even numbers, searching for reach value from 0 up to the length + 5
  ;; and returning the results in a list
  (defun range (m step)
    (loop for i from 0 below m by step
      collect i))
  (mapcar (lambda (x) (inf-search (range (* 2 n) 2) x)) (range (+ (* n 2) 5) 1)))
