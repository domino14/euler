;; According to problem statement only have to go to 28123.

(ns euler-23
  (:require [utils.arithmetic :refer [abundant?]]))

;; The abundant numbers between 24 and 28123 inclusive:
(def abundants (set (for [num (filter abundant? (range 12 28124))] num)))


(defn sum-2-abundants?
  "Is this the sum of 2 abundant numbers?
  :abundants is a set of numbers to look in
  :num is the number we're testing."
  [num abundants]
  ;; 'some' calls the anon function and returns true if there is a match.
  (some #(and (< % num) (contains? abundants (- num %))) abundants))

(println (reduce +
  (for [num (range 1 28124)
      :when (not (sum-2-abundants? num abundants))]
    num)))