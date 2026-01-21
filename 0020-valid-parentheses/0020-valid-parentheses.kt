import java.util.*

class Solution {
    fun isValid(s: String): Boolean {
        val stack = Stack<String>()
        val splitted = s.split("").filter { !it.isEmpty() }
        for (i in splitted) {
            if (stack.isEmpty()) {
                stack.push(i)
                continue
            }
            when (i) {
                ")" -> if (stack.peek() == "(") stack.pop() else stack.push(i)
                "]" -> if (stack.peek() == "[") stack.pop() else stack.push(i)
                "}" -> if (stack.peek() == "{") stack.pop() else stack.push(i)
                else -> stack.push(i)
            }
        }
        return stack.isEmpty()
    }
}