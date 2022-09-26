;; Scheme ;;


(define lst
 '((1) 2 (3 4) 5)
)

(define (composed f g)
  (lambda (x) (f(g x)))
)

(define (remove item lst)
  (cond
    ((null? lst) nil)
    ((= item (car lst)) (remove item (cdr lst)))
    (else (cons (car lst) (remove item (cdr lst))))
    )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  'YOUR-CODE-HERE
)

(define (substitute s old new)
  'YOUR-CODE-HERE
)


(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
