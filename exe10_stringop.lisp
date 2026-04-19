(defun run-demo ()
  ;;; --- 1. Dynamic String Concatenation ---
  (format t "--- 1. Concatenation ---~%")
  (format t "Enter first word: ")
  (force-output) ; Ensures the prompt appears before reading
  (let ((str1 (read-line)))
    (format t "Enter second word: ")
    (force-output)
    (let ((str2 (read-line)))
      (format t "Result: ~A~%~%" (concatenate 'string str1 " " str2))))

  ;;; --- 2. Dynamic Case Conversion ---
  (format t "--- 2. Case Conversion ---~%")
  (format t "Enter a phrase to convert: ")
  (force-output)
  (let ((my-str (read-line)))
    (format t "Uppercase: ~A~%" (string-upcase my-str))
    (format t "Lowercase: ~A~%" (string-downcase my-str))
    (format t "Capitalized: ~A~%~%" (string-capitalize my-str)))

  ;;; --- 3. Dynamic Substring Search ---
  (format t "--- 3. Search and Length ---~%")
  (format t "Enter a full sentence: ")
  (force-output)
  (let ((sentence (read-line)))
    (format t "Enter the word to find: ")
    (force-output)
    (let ((target (read-line)))
      (format t "Length of sentence: ~D~%" (length sentence))
      (let ((pos (search target sentence)))
        (if pos
            (format t "Position of '~A': ~D~%" target pos)
            (format t "'~A' not found in the sentence.~%" target))))))
