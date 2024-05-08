import java.util.*;
class Solution{
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input = sc.next();
            Stack<String> stack = new Stack<>();
            String rule1 = "({[";
            String rule2 = "])}";
            boolean flag = false;
            for(int i = 0;i < input.length();i++){
                String current = input.charAt(i) + "";
                if(rule1.contains(current)){
                    stack.push(current);
                }
                else {
                    try{
                    String popped = stack.pop();
                    if(popped.equals("(") && current.equals(")") ||
                    popped.equals("{") && current.equals("}") ||
                    popped.equals("[") && current.equals("]"))
                    {
                        continue;
                    }
                    else{
                        flag = true;
                        break;
                    }
                    }
                    catch(EmptyStackException emptyStackException){
                        flag = true;
                        break;
                    }
                } 
        }

        if(flag == true || !stack.isEmpty()){
            System.out.println(false);
        }else {
            System.out.println(true);
        }

            }
                
		}
}
