;; Scheme ;;

;helper
(define (filter-lst f lst)
  (cond
    ((null? lst) nil)
    ((f (car lst)) (cons (car lst) (filter-lst f (cdr lst))))
    (else (filter-lst f (cdr lst)))
    )
)
(define (is-in-lst item lst)
  (cond
    ((null? lst) #f)
    ((= item (car lst)) #t)
    (else (is-in-lst item (cdr lst)))
    )
  )

(define lst
 '((1) 2 (3 4) 5)
)

(define (composed f g)
  (lambda (x) (f(g x)))
)

(define (remove item lst)
  (filter-lst (lambda (x) (not (= item x))) lst)
)



;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)



(define (no-repeats s)
    (
        cond 
                 ((null? s) nil)
                 ((is-in-lst (car s) (cdr s)) (cons (car s) (no-repeats (remove (car s) (cdr s)))))
                 (else (cons (car s) (no-repeats (cdr s))))
                 
    )    
)
(define (substitute s old new)
  'YOUR-CODE-HERE
)


(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
