import java.util.*;

class MyQueue {
    private Stack<Integer> oldest;
    private Stack<Integer> newest;

    public MyQueue() {
        this.oldest = new Stack<>();
        this.newest = new Stack<>();
    }
    
    public void push(int x) {
        newest.push(x);
    }

    private void shiftStacks() {
        if (oldest.isEmpty()) {
            while(!newest.isEmpty()) {
                oldest.push(newest.pop());
            }
        }
    }
    
    public int pop() {
        shiftStacks();
        return oldest.pop();
    }
    
    public int peek() {
        shiftStacks();
        return oldest.peek();
    }
    
    public boolean empty() {
        return oldest.isEmpty() && newest.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */