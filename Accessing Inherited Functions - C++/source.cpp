class D :public A,public B,public C
{
    private:
    int count_2,count_3,count_5;
	int val;
    void check_factor(int new_val){
         for(;new_val != 0;){
             if(new_val == 1){
                 return;
             }
               if(new_val % 2 == 0){
                   new_val /= 2;
                   count_2++;
               }
               if(new_val % 3 == 0){
                   new_val /= 3;
                   count_3++;
               }
              if(new_val % 5 == 0){
                   new_val /= 5;
                   count_5++;
               }
         }
    }
	public:
		//Initially val is 1
		 D()
         :count_2(0),count_3(0),count_5(0)
		 {
		 	val = 1;
		 }


		 //Implement this function
		 void update_val(int new_val)
		 {
             check_factor(new_val);
             for(int i = 1;i <= count_2;i++){
                 A::func(val);
             }
              for(int i = 1;i <= count_3;i++){
                 B::func(val);
             }
              for(int i = 1;i <= count_5;i++){
                 C::func(val);
             }
			
		 }
		 //For Checking Purpose
		 void check(int); //Do not delete this line.
};
