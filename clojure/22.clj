(defn strip-quotes
  "Strip the quote characters from a string."
  [str]
  (clojure.string/replace str #"\"" "")
)

(defn score
  "Computes a 'score' for a string, given a position."
  [pos str]
  (* pos (reduce + (for [chr (seq str)
                         :let [val (- (int chr) (- (int \A) 1))]]
                    val)))

)

(defn get-sorted-strs
  "Reads the file and returns sorted strings from it."
  []
  (sort (map strip-quotes (clojure.string/split (slurp "22_names.txt") #",")))
)

(println (reduce + (let [strs (get-sorted-strs)]
                    (map score (range 1 (+ 1 (count strs))) strs)
)))





