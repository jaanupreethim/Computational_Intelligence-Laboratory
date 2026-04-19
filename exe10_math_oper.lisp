(defun run-math-demo ()
  (format t "--- GCD and LCM Calculator ---~%")

  (format t "Enter first number: ")
  (force-output)
  (let ((num1 (read)))

    (format t "Enter second number: ")
    (force-output)
    (let ((num2 (read)))

      ;; Calculate GCD (Greatest Common Divisor / GCM)
      (let ((gcm-result (gcd num1 num2))
            ;; Calculate LCM (Least Common Multiple / LCD)
            (lcd-result (lcm num1 num2)))

        (format t "~%Results for ~D and ~D:~%" num1 num2)
        (format t "GCM (Greatest Common Measure): ~D~%" gcm-result)
        (format t "LCD (Lowest Common Denominator): ~D~%" lcd-result)))))
