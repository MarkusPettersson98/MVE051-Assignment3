(require '[clojure.string :as string])

(def book
  (slurp "roda_rummet.txt"))

(defn words [text]
  (string/replace text
                  #"[^äåöÄÅÖéÉ\w]+"
                  " "))

(defn split-at-whitespace [text]
  (string/split text #"\s+"))

(defn clean-text [text]
  (-> text
      (words)
      (string/lower-case)
      (string/trim)))

(defn words-list [text]
  (split-at-whitespace
   (clean-text text)))

(defn count-words [text]
  (count
   (words-list text)))

;; This function is cool 
(defn group-unique-words [text]
  (-> text
      (words-list)
      (frequencies)))


;; ----------- VARIABLES -----------
(def unique-words-in-book
  (group-unique-words book))

;; Count all words in the book
(def word-count-1
  (count-words book))

;; Count all words by summing all occurences of all
;; unique words
(def word-count-2
  (reduce +
          (map second unique-words-in-book)))

;; Check if they are the same!
(= word-count-1 word-count-2)

(group-unique-words book)

;; Map of all the unique words. 
;; Key = word
;; Value = Number of times the words occurences
;;  (println 
;;    (take 10
;;      (sort-by second > unique-words-in-book))) ;; Sort by values of map descending order
