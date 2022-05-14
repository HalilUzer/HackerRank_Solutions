

class Person
{
protected:
    string name;
    int age;
    public:
    Person():age(0),name("0"){}
    virtual void getdata(){
        cin >> name >> age;
    }
    virtual void putdata(){
        cout << name << " " <<age;
    }
};

class Professor:public Person{
private:
    int publications;
    static int cur_idx;
    int cur_id;
public:
    Professor():publications(){cur_id = cur_idx,cur_idx++;}
    void getdata() override{
        cin >> name >> age >> publications;
    }
    void putdata()override{
        cout  << name << " " << age << " " << publications << " " << cur_id << endl;
    }
};

class Student:public Person{
    private:
    int marks[6];
     static int cur_idx;
     int cur_id;
    public:
   Student():Person(){cur_id = cur_idx,cur_idx++;}
    void getdata()override{
        cin >> name >> age;
        for(int i = 0;i < 6;i++){
            cin >> marks[i];
        }
    }
    void putdata()override{
        int sum = 0;
        cout << name << " " << age << " ";
        for(int i = 0;i < 6;i++){
            sum += marks[i];
        }
        
        cout << sum << " " << cur_id << endl;
    }
};

int Student::cur_idx = 1;
int Professor::cur_idx = 1;
