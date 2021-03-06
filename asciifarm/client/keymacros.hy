

(defmacro send [data]
    `(self.client.send ~data))

(defmacro inp [action]
    `(send ["input" ~action]))

(defmacro move [dir]
    `(inp ["move" ~dir]))

(defmacro say [text]
    `(inp ["say" ~text]))

(defmacro log [text]
    `(self.client.log ~text))

(defmacro chat [text]
    `(send ["chat" ~text]))

(defmacro doall [actions]
    `(for [action ~actions] (action)))

(defmacro selector [name]
    `(self.display.getSelector ~name))

(defmacro selectorvalue [name]
    `(.getValue (selector ~name)))

(defmacro log [text]
    `(self.client.log ~text))
