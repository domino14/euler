(println "started")
(defn permutations [items]
  (if (= 1 (count items))
    [items]
    (apply concat
      (for [item items
            :let [perms-without-item (permutations (remove #{item} items))]]
        (for [perm perms-without-item]
          (conj perm item))))))

(def i 999999)
(def els 10)

(println (nth (sort (map clojure.string/join (permutations (range 0 els)))) i))
;; This didn't actually work. it is horribly inefficient. This problem can be
;; done by hand, or with python:
;; for perm in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
;;     l.append(''.join(map(str, perm)))
;; l.sort()
;; l[999999]
;; i ended up doing it by hand and was off by 1 since i accidentally divided
;; 1000000 instead of 999999.