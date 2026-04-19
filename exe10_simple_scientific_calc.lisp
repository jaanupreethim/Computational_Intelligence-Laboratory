(defun scientific-calculator ()
  (let ((deg-to-rad (/ pi 180))) ; Constant to convert degrees to radians
    (format t "--- Scientific Calculator (Trig in Degrees) ---~%")
    (format t "Operations: add, sub, mul, div, sin, cos, tan, sqrt, exp, exit~%")
    (loop
      (format t "~%Enter operation: ")
      (force-output)
      (let ((op (read)))
        (case op
          ((add sub mul div)
           (format t "Enter first number: ") (force-output)
           (let ((n1 (read)))
             (format t "Enter second number: ") (force-output)
             (let ((n2 (read)))
               (format t "Result: ~A~%"
                       (case op
                         (add (+ n1 n2))
                         (sub (- n1 n2))
                         (mul (* n1 n2))
                         (div (if (/= n2 0) (/ n1 n2) "Error: Division by zero")))))))

          ((sin cos tan)
           (format t "Enter angle in DEGREES: ") (force-output)
           (let ((n (read)))
             (format t "Result: ~F~%" ; ~F formats as a float
                     (case op
                       (sin (sin (* n deg-to-rad)))
                       (cos (cos (* n deg-to-rad)))
                       (tan (tan (* n deg-to-rad)))))))

          ((sqrt exp)
           (format t "Enter number: ") (force-output)
           (let ((n (read)))
             (format t "Result: ~A~%"
                     (case op
                       (sqrt (sqrt n))
                       (exp (exp n))))))

          (exit (return (format t "Exiting...~%")))
          (t (format t "Invalid operation.~%")))))))
