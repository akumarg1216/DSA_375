/**
 * Implement Stack Queue using Deque_5
 */
public class ImplementStackQueueusingDeque_5 {

    static class DQNode{
        int value;
        DQNode next;
        DQNode prev;
    }

    static class deque{
        private DQNode head;
        private DQNode tail;

        public deque(){
            head = tail = null;
        }

        boolean isEmpty(){
            if (head==null)
                return true;
            else
                return false;
        }

        int size(){
            if(!isEmpty()){
                DQNode temp = head;
                int len = 0;

                while(temp!=null){
                    len++;
                    temp = temp.next;
                }
                return len;
            }
            return 0;
        }

        void insert_first(int element){
            DQNode temp = new DQNode();
            temp.value = element;

            if(head == null){
                head = tail = temp;
                temp.next = temp.prev = null;
            }

            else{
                head.prev = temp;
                temp.next = head;
                temp.prev = null;
                head = temp;
            }
        }

        void insert_last(int element){
            DQNode temp = new DQNode();
            temp.value = element;
            
            if (head == null){
                head = tail = temp;
                temp.next = temp.prev = null;
            }
            else{
                tail.next = temp;
                temp.next = null;
                temp.prev = tail;
                tail = temp;
            }
        }

        void remove_first(){
            if(!isEmpty()){
                DQNode temp = head;
                head = head.next;
                head.prev = null;

                return;
            }
            System.out.println("List is Empty. Cannot pop...");
        }

        void remove_last(){
            if(!isEmpty()){
                DQNode temp = tail;
                tail = tail.prev;
                tail.next = null;

                return;
            }
            System.out.println("List is Empty. Cannot pop2...");
        }

        void display(){
            if(!isEmpty()){
                DQNode temp = head;
                while(temp!=null){
                    System.out.println(temp.value + " ");
                    temp = temp.next;
                }
                return;
            }
            System.out.println("List is empty. Nothing to display");
        }
    }

    static class Stack{
        deque d = new deque();
        
        public void push(int element) {
            d.insert_last(element);
        }

        public int size(){
            return d.size();
        }

        public void pop(){
            d.remove_last();
        }

        public void display(){
            d.display();
        }
    }

    static class Queue{
        deque d = new deque();

        public void enqueue(int element){
            d.insert_last(element);
        }

        public void dequeue(){
            d.remove_first();
        }

        public void display(){
            d.display();
        }

        public int size(){
            return d.size();
        }
    }

    public static void main(String[] args) {
        Stack stk = new Stack();

        stk.push(7);
        stk.push(8);
        System.out.print("Stack: ");
        stk.display();

        System.out.println();
     
        // pop an element
        stk.pop();
        System.out.print("Stack: ");
        stk.display();
    
        // For new line
        System.out.println();
    
        // Object of Queue
        Queue que = new Queue();
    
        // Insert 12 and 13 in queue
        que.enqueue(12);
        que.enqueue(13);
        System.out.print("Queue: ");
        que.display();
    
        // New line
        System.out.println();
        
        // Delete an element from queue
        que.dequeue();
        System.out.print("Queue: ");
        que.display();
    
        // New line
        System.out.println();
        System.out.println("Size of stack is " +
                        stk.size());
        System.out.println("Size of queue is " +
                        que.size());
    }
}