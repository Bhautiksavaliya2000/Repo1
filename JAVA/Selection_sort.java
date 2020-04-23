import java.util.Scanner;

 class Selection_sort
{
  public static void main(String []args)
  { 
    int i,j,no;

    // Reading total number of element.
    
    System.out.println("Enter total number of elements :");
    
    Scanner in_no = new Scanner(System.in);    // object for total no of element
    no = in_no.nextInt();

    int arr[] = new int[no];

    //Reading values from the user.
   
     Scanner input = new Scanner(System.in);    // object for reading element
    
    System.out.println("Enter all the elemnts with enter key");
    for(i=0;i<arr.length;i++)
         arr[i] = input.nextInt();
      
     //  selection sorting.
    System.out.println("The shorted list is :");
    for(i=0;i<arr.length;i++)
     {
       for(j=i+1;j<arr.length;j++)
       {
         if(arr[i]>arr[j])
         {
           arr[i] = arr[i]+arr[j];
           arr[j] = arr[i]-arr[j];
           arr[i] = arr[i]-arr[j];
         }
       }
     }
    for(i=0;i<arr.length;i++)
     System.out.println(arr[i]);
  }
}
