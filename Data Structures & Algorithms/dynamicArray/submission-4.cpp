class DynamicArray {
public:

    DynamicArray(int capacity_) {
            container = new int [capacity_];
            capacity = capacity_;
            size = 0;
    }
    ~DynamicArray()
    {

    }

    int get(int i) {
        return container[i];
    }

    void set(int i, int n) {
        container[i] = n ;
    }

    /*
         Push back and element at 
         the end of the array.

                                         
          0 1 2 3 4 5 6 7 8 
         [4,0,0,0,0,0,0,0,0]
    */
    void pushback(int n) {
        if(size == capacity){
            resize();
        }
        container[size] = n ;
        size+=1;
         printf("%d first print \n",size);
    }
    /* 
        Remember this is a soft deletion
    */
    int popback() {
        int poppedElement = container[size-1];
        printf("%d second print popped \n",poppedElement);
        printf("%d second print \n",size);
        size-=1;
        return poppedElement;
    }

    void resize() {
       this->capacity *=2;
       int* oldarray = container; 
       container = new int [this->capacity];
       for (int i = 0; i < size; i++)
       {
         container[i] = oldarray[i];
       }
       delete oldarray;

    }

    int getSize() {
        printf("%d third print \n",size);
        return this->size;
    }

    int getCapacity() {
        return this->capacity;
    } 
private:
    int capacity;
    int size; 
    int end; 
    int* container = nullptr;
};
