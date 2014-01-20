;;;; Utility functions to deal with vectors and Euclidean geometry.
(ns utils.vector-math)

(defn magnitude
  "Magnitude of vector."
  [v]
  (Math/sqrt (+ (* (first v) (first v)) (* (second v) (second v)))))

(defn dot
  "Dot product of two vectors."
  [A B]
  (+ (* (first A) (first B)) (* (second A) (second B))))

(defn cos-theta
  "Cosine of angle between two vectors."
  [A B]
  (/ (dot A B) (* (magnitude A) (magnitude B))))


(defn euclidean-distance
  "Euclidean distance between two points."
  [pt1 pt2]
  (Math/sqrt (+
    (* (- (first pt1) (first pt2)) (- (first pt1) (first pt2)))
    (* (- (second pt1) (second pt2)) (- (second pt1) (second pt2))))))