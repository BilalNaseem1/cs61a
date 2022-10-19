(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))



;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
      (define (make-enumerate lst index)
        (if (null? lst)
            nil
            (cons (list index (car lst)) (make-enumerate (cdr lst) (+ index 1))))
        )(make-enumerate s 0)
      )
  ; END PROBLEM 17

;; Problem 18

(define (zip pairs)
  ; BEGIN PROBLEM 18
    (define (zipped-tail pairs lst)
             (if (null? pairs)
                 lst
                 (zipped-tail (cdr pairs)
                 (list
                (append (car lst) (list (car (car pairs))))
                (append (car (cdr lst)) (cdr (car pairs)))             
                    )
                )
             )
         )(zipped-tail pairs '(() ()))
  )
  ; END PROBLEM 18


;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr))) ; BEGIN PROBLEM 19
           (append `(,(let-to-lambda form) ,(map let-to-lambda params)) (let-to-lambda body))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (car(cddr expr))))
           ; BEGIN PROBLEM 19
           'replace-this-line
           (define zipped-vals (zip values))
           (define params (car zipped-vals))
           (define args (car (cdr zipped-vals)))
           
           (append `((lambda ,( map let-to-lambda params)
            ,(let-to-lambda body)
         
           ; END PROBLEM 19
           )) (let-to-lambda args))
       ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
(define first-let '(let ((a 1) (b 2)) (+ a b)))

(define first-lambda '(lambda (let a b) (+ let a b)))

(define second-let '(let ((a (let ((a 2)) a))
                 (b 2))
                (+ a b)))

