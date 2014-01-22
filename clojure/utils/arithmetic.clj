(ns utils.arithmetic)

(defn divisors
  "The proper divisors of n."
  [num]
  (flatten (for [i (range 1 (inc (Math/floor (Math/sqrt num))))
        :when (= (mod num i) 0)]
    (if (and (not= i 1) (not= num (* i i))) [i (/ num i)] [i]))))

(defn d_n
  "The sum of proper divisors of n."
  [num]
  (reduce + (divisors num)))

(defn abundant?
  "Is this an abundant number? (Do the sum of its proper divisors exceed it?)"
  [num]
  (> (d_n num) num))