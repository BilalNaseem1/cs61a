(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)


(define (rle s)
    (define (compress strm prev count)
        (if (or (null? strm) (not (= prev (car strm))))
            (cons-stream (list prev count) (rle strm))
            (compress (cdr-stream strm) prev (+ 1 count))
        )
    )
    
    (if (null? s)
        nil
        (compress  (cdr-stream s) (car s) 1))
)
