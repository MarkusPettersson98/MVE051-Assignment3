(require '[clojure.string :as string])

(def book
  (slurp "texts/red_room.txt"))

(defn words [text]
  (-> text
      (remove-apostrophes)
      (#(string/replace %
                        #"[^äåöÄÅÖéÉ\w]+"
                        " "))))

(defn split-at-whitespace [text]
  (string/split text #"\s+"))

(defn remove-apostrophes [text]
  (string/replace text
                  #"'+"
                  ""))

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

(defn sort-map [map]
  (sort-by second > map))

;; This function is cool 
(defn group-unique-words [text]
  (-> text
      (words-list)
      (frequencies)))


;; ----------- VARIABLES -----------
(def unique-words-in-book
  (group-unique-words book))

;; Zipfs law
(defn zipfs [text]
  (let [most-common-word (first text)
        occurences-most-common-word (second most-common-word)])
  (map-indexed (fn [index word]
                ;; Do something with index
                 (let [rang (+ 1 index)]
                   (zipmap index word)))
               text))

;; Check Zipfs law on the n most common words
(defn zipfs-map [coll n]
  (take n
        (sort-map
         coll)))

(zipfs-map unique-words-in-book 25)


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