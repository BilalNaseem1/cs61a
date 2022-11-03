; Lab 14: Final Review

(define (compose-all funcs)
    (lambda (x) (if (null? funcs)
                    x
                    (
                     (compose-all (cdr funcs))
                     ((car funcs) x)
                     )
                )
      )
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond (_________________ ____________)
          (_________________ ____________)
          (else _________________________))
    )
  ______________________________
)

(define (contains? lst s)
  'YOUR-CODE-HERE
)
