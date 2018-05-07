;; Linked List Exercises - May 4, 2018.
;;
;;        Take a list of integers and rearrange it so all the even integers
;;             appear before all the odd integers, with both evens and odds
;;             appearing in the output in the same order as the input. 
;;        Take a list of integers, split it into two lists each containing
;;             alternate elements from the input list, then join the two lists
;;             back together. 
;;        Take a list of integers and rearrange it so alternate nodes are each
;;             greater than their two adjacent nodes; in other words, the
;;             integers are in alternating high-low order. 
;; 

(defun evens-before-odds (numbers)
  (let ((evens (loop :for n in numbers
          :when (evenp n)
          :collect n))
        (odds (loop :for n in numbers
          :when (oddp n)
          :collect n)))
    (nconc evens odds)))

;; Improved implementation with better use of the loop macro.
(defun evens-before-odds2 (numbers)
  (loop :for n :in numbers
          :when (evenp n) :collecting n :into evens
          :when (oddp n) :collecting n :into odds
	  :finally (return (nconc evens odds))))

;; Note: programming-praxis' more elegant solution:
(defun evens-before-odds-3 (numbers)
  (append (remove-if-not #'evenp numbers) (remove-if-not #'oddp numbers)))


(defun unzipper-list (items)
  (loop :for n in  items
        :for i :from 0
        :when (evenp i) :collecting n :into evens
        :when (oddp i) :collecting n :into odds
        :finally (return (nconc evens odds))))

(defun zipper (l1 l2)
  (loop :for m in  l1
        :for n in  l2
        ;:collecting (list m n) :into pairs
        :appending (list m n) :into pairs
        :finally (return pairs)))

; e.g.
; (1 2 3 4 5 6 7 8 9) =>
; (1 3 2 5 4 7 6 9 8)
; or
; (2 1 4 3 6 5 8 7 9)
(defun alternating-peaks (items)
  (loop :for n in (sort items #'<)
        :for i :from 0
        :when (evenp i) :collecting n :into evens
        :when (oddp i) :collecting n :into odds
	:finally (return (zipper odds evens))))
