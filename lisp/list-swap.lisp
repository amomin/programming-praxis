;;;; List Swap
;;;; December 13, 2016

;;; Given a list and an integer, sway the kth and kth last items.  For example,
;;; for list = (1 2 3 4 5 6 7) and k = 2, the result should be
;;; (1 6 3 4 5 2 7).

(defun list-swap-1 (list k)
  ;; Using setf
  (let ((tmpa (nth (- k 1) list))
	(tmpb (nth (- (length list) k ) list)))
      (setf (nth (- k 1) list) tmpb)
      (setf (nth (- (length list) k) list) tmpa)
      list))

(defun list-swap-2 (list k)
  ;; Fails to consider the case where k is larger than half the
  ;; list.  I'm going to leave it out since I'm still learning
  ;; lisp basics though.  I'm almost certain this isn't in-place
  ;; either, so clearly quite a bit left to learn...
  (let ((kth-element nil)
	(kth-last-element nil)
	(r '())
	(tail '())
	(front '())
	(mid '()))
    (loop for i from 0 below (- k 1) do
	 (setf front (append front (list (car list))))
	 (setf list (cdr list)))
    (setf kth-element (car list)) ; We have the first item in the swap (recall assumption)
    (setf list (cdr list))
    (setf r list) ; Forward pointer, advance by k places
    (do ((i 0 (1+ i))) ((= i k) nil)
      (setf r (cdr r)))
    (do () ((null r) nil) ; advance both current and forward pointers, building the middle of the result
      (setf mid (append mid (list (car list))))
      (setf list (cdr list))
      (setf r (cdr r)))
    (setf kth-last-element (car list)) ; Second item in the swap
    (setf tail (cdr list)) ; Set the tail to what's after this item - ready to return
    (append front (list kth-last-element) mid (list kth-element) tail)))
