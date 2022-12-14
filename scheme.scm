(cons 1 2)  ; pairs, 显示为(1 . 2)
(cons 1 (cons 2 nil))  ;scheme 当中的list，即nest list，显示为(1 2)
(list 1 2) ;与上行代码等价

;symbolic programming
(define a 1)
(define b 2)
(list a b) ;get (1 2)
(list 'a 'b) ; get (a b),其中a，b是symbol，而不是character, symbol can be evaluated. see example below
(cdr '(a b c))   ;get (b c)

(define func 1)
(eval 'func) ;you get 1
(list? '(1 2)) ; you get true!
(equal? '(1 2) (list 1 2))   ;这两个list的内容相同
;The quote special form takes in a single operand. It returns this operand
; exactly as is, without evaluating it. Note that this special form can be used
; to return any value, not just a list.
(car '(1 2)) ;不会报错，因为有了single quote，(1 2)不会被evaluate
(car (1 2)) ;会报错，这是一个call expression，operand需要被evaluate，而(1 2)被evaluate的话会报错
(car (list 1 2)) ;不会报错，(list 1 2)被evaluate后得到(1 2), 其第一个元素是1











; 我们implement的scheme interpreter中，没有专用的循环syntax。我们用递归函数实现循环的功能。但是，递归占用的空间（On）可能比一般的while、for循环占用的空间（O1）要多，因此我们用到尾递归（tail recursion）
;The return value of the tail call is the return value of the current procedure call .
; Therefore, tail calls shouldn't increase the environment size







; 递归 see https://www.youtube.com/embed/a9HkM2DaCYE for more information.
; 看一个计算阶乘的例子
(define (factorial n) ; n!
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))

; try (factorial 1000), we will get RecursionError('maximum recursion depth exceeded') error.
; not tail recursion


(define (factorial_tail1 n) ;这是从后往前的尾递归
  (define (factorial_tail1_helper m sofar)
    (if (= m 1)
        sofar
        (factorial_tail1_helper (- m 1) (* m sofar))))
  (factorial_tail1_helper n 1))


(define (factorial_tail2 n)  ;这是从前往后的尾递归
  (define (factorial_tail2_helper m sofar)
    (if (= m n)
        sofar
        (factorial_tail2_helper (+ m 1) (* (+ m 1) sofar))))
  (factorial_tail2_helper 1 1))








;macros allow you to extend that inventory by inventing new kinds of special forms. That means we can change 
;the way the language works. Inventing new ways in which the flow of evaluation proceeds though a program.
; 普通的procedure先evaluate operator，然后print 返回值；macro procedure 不evaluate operator，得到返回值后再evaluate，最后print。
;理解下面代码中eval的过程
(define (twice expr)  (list 'begin expr expr) )
(twice (print 2)) ;(print 2)作为operand,被evaluate,打印一个2，函数返回值为(begin None None),再次被evaluate报错
(eval (twice '(print 2))) 

(define-macro (twice expr) (list 'begin expr expr))
(twice (print 2)) ; scheme evaluate operator 'twice',发现它是一个macro函数，于是它不evaluate operand，
;(twice (print 2)) 得到的返回值是(begin (print 2)  (print 2)),返回值被evaluate，打印两个2

;Evaluation procedure of a macro call expression: 
;• Evaluate the operator sub-expression, which evaluates to a macro 
;• Call the macro procedure on the operand expressions without evaluating them first 
;• Evaluate the expression returned from the macro procedure

;Evaluation procedure of a normal call expression(same in Python): 
;• Evaluate the operator and operand. 
;• Call the procedure on the operand expressions after evaluating them  
;• return the expression from the procedure


;We evaluated lambda procedures in the following way:
;1. Evaluate operator
;2. Evaluate operands
;3. Apply operator to operands, evaluating the body of the procedure
;However, the rules for evaluating calls to macro procedures are:
;1. Evaluate operator
;2. Apply operator to unevaluated operands
;3. Evaluate the expression returned by the macro in the frame it was called in.












;利用macro定义for循环语句
(define (map fn vals)
	(if (null? vals)
		()
		(cons (fn (car vals)) (map fn (cdr vals)))))

(map (lambda (x) (* x x)) '(2 3 4 5))

(define-macro (for sym vals expr) ;法1
	(list 'map (list 'lambda (list sym) expr) vals))

(define-macro (for sym vals expr) ;法2
	`(map (lambda (,sym) ,expr) ,vals) ; 等价于'(map (lambda (x) (* x x)) '(1 2 3))
)

(for x '(1 2 3) (* x x))


