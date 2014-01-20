;;; Ellipse described by 4x^2 + y^2 = 100
;;; The tangent slope on any point is m = -4x/y; meaning the normal slope is
;;; y/4x.

;;; a dot b = |a| |b| cos theta
;;; cos theta = a dot b / (|a| |b|)

;;; Intersection of ellipse and line
;;; y = m(x - x1) + y1 -> plug into ellipse equation above
;;; Result:2
;;; x = (-mb +/- 2 * sqrt(-b^2 + 25m^2 + 100)) / (m^2 + 4)
;;; y = mx + b
;;; where b = y1 - mx1

(ns euler-144
  (:require [utils.vector-math :refer [magnitude dot cos-theta
                                       euclidean-distance]]))

(def EPSILON 1e-8)

(defn ellipse-line-inter
  "The intersection points between a line and the ellipse."
  [m x1 y1]
  ;; b = y-intercept = y1 - mx1
  (let [b (- y1 (* m x1))       ; y-intercept
        disc (+ (- (* b b)) (* 25 m m) 100) ; discriminant (sort-of)
        den (+ (* m m) 4) ; denominator
        tmp (* 2 (Math/sqrt disc)) ; 2 * the square root of discriminant.
        x-plus (/ (+ (* (- m) b) tmp) den)
        x-minus (/ (- (* (- m) b) tmp) den)]
    [[x-plus (+ (* m x-plus) b)] [x-minus (+ (* m x-minus) b)]]))

(defn pts-to-vector
  "Given a start and a finish point, finds the vector start->finish."
  [start finish]
  [(- (first finish) (first start)) (- (second finish) (second start))])

(defn pt-slope-to-vector
  "Given a point, and a slope, makes a vector from point with that slope.
  The slope is a y x vector, instead of a float. (So it can be calculated as
  y/x)."
  [pt slope]
  [(+ (first pt) (second slope)) (+ (second pt) (first slope))])

(defn normal-slope
  "Returns a [y x] pair denoting the slope of the normal at the given [X Y]
  point"
  [pt]
  [(second pt) (* 4 (first pt))])

(defn rotate-vec-twice
  "Given a vector, a cosangle, and a sinangle, rotates vector by twice the
  angle."
  [vc cosangle sinangle]
  ;; The formulae are
  ;; x' = (x costheta - y sintheta) costheta - (x sintheta + y costheta) sintheta
  ;; y' = (x costheta - y sintheta) sintheta + (x sintheta + y costheta) costheta
  (let [term1 (- (* (first vc) cosangle) (* (second vc) sinangle))
        term2 (+ (* (first vc) sinangle) (* (second vc) cosangle))
        x-prime (- (* term1 cosangle) (* term2 sinangle))
        y-prime (+ (* term1 sinangle) (* term2 cosangle))]
    [x-prime y-prime]))

(defn pts-close-enough?
  "Returns true if the Euclidean distance between two points is 'close enough'."
  [pt1 pt2]
  (< (euclidean-distance pt1 pt2) EPSILON)
)

(defn escaped-hole?
  "Did the laser beam go through the hole at the top (-0.01 <= x <= 0.01)?"
  [pt]
  (and (<= -0.01 (first pt) 0.01) (> (second pt) 0))
)

(defn next-point
  "Given a first pt and a second pt, finds the next intersection on ellipse and
  the vector pointing at this intersection point."
  [pt-1 pt-2]
  ;; Find the normal at pt-2
  (let [nslope (normal-slope pt-2)
        nvec [(second nslope) (first nslope)]
        incident-vec (pts-to-vector pt-1 pt-2)
        flipped-vec [(- (first incident-vec)) (- (second incident-vec))]
        cosangle (cos-theta incident-vec nvec)
        sinangle (Math/sqrt (- 1 (* cosangle cosangle)))
        reflected-vec (rotate-vec-twice flipped-vec cosangle sinangle)
        ;; reflected-vec is the final reflected vector. Find out where this
        ;; hits the ellipse.
        reflected-slope (/ (second reflected-vec) (first reflected-vec))
        inter-pts (ellipse-line-inter reflected-slope (first pt-2)
                   (second pt-2))]
    ;; Since there are two intersection points we need to throw one out, the
    ;; one that is basically pt-2.
    ;; XXX: I don't really like this. There should be a way to figure out which
    ;; intersection point to throw away from the math.
    (if (pts-close-enough? (first inter-pts) pt-2)
      [(second inter-pts) reflected-vec]
      [(first inter-pts) reflected-vec])))

;; Numerical errors galore, I hope this works.
(loop [pt1 [0 10.1]
       pt2 [1.4 -9.6]
       reflect-count 1]
  (println "Reflection" reflect-count pt2)
  (let [nxt (next-point pt1 pt2)
        nxt-pt (first nxt)]   ; nxt is a vector [point, incident_vec]
    (if (not (escaped-hole? nxt-pt))
      (recur pt2 nxt-pt (inc reflect-count))
      (println "Escaped hole after" reflect-count "bouncies. (" nxt-pt ")"))))

