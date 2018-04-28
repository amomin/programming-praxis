(defun sum-square-digits (n)
  "Shoud loop but I don't know how, so I'll use recursion."
  (labels ((helper (n collector)
		  (if (> n 0)
		      (let ((m (mod n 10))
			    (q (floor (/ n 10))))
			(helper q (+ collector (* m m))))
		      collector)))
	 (helper n 0)))



(defun ssds (n)
  "Compute the sequence up to termination at 1 or 4."
  (cond ((< n 1) '"NonPosiiveArgumentException")
	((eql n 1) '(1))
	((eql n 4) '(4))
	('t (cons n (ssds (sum-square-digits n))))))

(defun happy? (n)
  "Determine if a number is happy or not."
  (cond ((< n 1) '"NonPosiiveArgumentException")
	((eql n 1) 't)
	((eql n 4) nil)
	('t (happy? (sum-square-digits n)))))
