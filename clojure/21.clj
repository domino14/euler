(defn divisors
  "The proper divisors of n."
  [num]
  (for [i (range 1 (+ (quot num 2) 1))
        :when (= (mod num i) 0)]
   i)
)

(defn d_n
  "The sum of proper divisors of n."
  [num]
  (reduce + (divisors num))
)


(defn map_create
  "The map of all numbers under x with their d(n)."
  [num]
  (into {} (for [i (range 1 num)
      :let [y (d_n i)]]
      [i y]))
)

(defn amicables?
  "Given a map and two numbers, tells you if the numbers are amicable."
  ([num_map i j]
    (and (not= i j) (= i (get num_map j)) (= j (get num_map i))))
  ([num_map vc]
    (amicables? num_map (first vc) (second vc))
  )
)

(defn find_amicables
  "Given a map of {n d(n)}, find the amicables."
  [num_map]
  (for [vc (filter (partial amicables? num_map) num_map)
      :let [f (first vc)]]
      f)
)

; Evaluate sum of all amicable numbers under 10000.

(println (reduce + (find_amicables (map_create 10000))))
