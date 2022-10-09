;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (remove-item s item)
    (filter (
            lambda (x) (not(eq? x item))
            )
    s
    )
)

(define (unique s)
    (if (null? s)
    nil
    (cons (car s) (unique(remove-item s (car s))))
    )
)


(define (cons-all first rests)
  (map (lambda (rest) (cons first rest)) rests)
  )

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
    (cond
        ((> 0 total) nil)
        ((null? denoms) nil)
        ((= 0 total) (list ()))
        (else (append(cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))
        ) 
) 

; Tail recursion

(define (replicate x n)
    (define (replicate-tail x curr-len accumulator)
        (if (= n curr-len)
            accumulator
            (replicate-tail x (+ curr-len 1) (append accumulator (list x)))
            )
        )
    (replicate-tail x 0 (list))
    )

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)