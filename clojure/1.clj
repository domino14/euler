(defn multiple-35?
  "Is the passed in number a multiple of 3 or 5?"
  [num]
  (or (= (mod num 3) 0) (= (mod num 5) 0))
)

(defn multiples-35-below
  "Find all multiples of 3 or 5 below the given parameter."
  [num]
  (for [i (range num)
        :when (multiple-35? i)]
    i
  )
)

(println (reduce + (multiples-35-below 1000)))