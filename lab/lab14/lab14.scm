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

(define (contains? lst s)
    (cond
        ((null? lst) #f)
        ((eq? (car lst) s) #t)
        (else (contains? (cdr lst) s))
        )
    )


(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          ;we basically create a list of pointers
          (else (pair-tracker (append seen-so-far (list curr)) (cdr-stream curr)))
    ))
  (pair-tracker (list s)  (cdr-stream s))
)

