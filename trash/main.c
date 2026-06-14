#include <stdio.h>
int main() {
     float salary, bonus = 0, final_salary;
     int experience, rating;

     printf("Enter salary: ");
     scanf("%f", &salary);
     printf("Enter years of experience: ");
     scanf("%d", &experience);
     printf("Enter performance rating: ");
     scanf("%d", &rating);

     if (experience >= 5) {
         if (rating == 5) {
             bonus = salary * 0.20;}
         else if (rating == 4) {
             bonus = salary * 0.15;}
         else {
             bonus = salary * 0.10;}}
     else {
         if (rating == 5) {
             bonus = salary * 0.10; }
         else if (rating == 4) {
             bonus = salary * 0.07;}
         else {
             bonus = salary * 0.05;}}

     final_salary = salary + bonus;
     printf("Bonus: %.0f\n", bonus);
     printf("Final Salary: %.0f\n", final_salary);

     return 0;
}
