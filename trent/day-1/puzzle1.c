#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int dialValue;
    int max;
    int min;
    FILE* fptr;
    char input[10];
    int pswd;
    int prevDialValue;
} dial_state;

int findNextValue(dial_state* dial){
    char direction[2];
    int number;

    if (sscanf(dial->input, "%c%d",direction,&number) == 2){
        dial->prevDialValue=dial->dialValue;

        if(number >= 100){
            int post_div = number / 100;
            int subtract_val = post_div * 100;
            number-=subtract_val;
            dial->pswd+=post_div;
            //printf("%s, PLUS QUOTIENT %c\n", dial->input,direction[0]);
        }

        if (direction[0] == 'L'){
            dial->dialValue -= number;
            if (dial->dialValue == 0){
                dial->pswd++;
            }
            if (dial->dialValue < dial->min){
                if (dial->prevDialValue != 0){
                    dial->pswd+=1;
                }
                dial->dialValue+= (dial->max+1);
                //printf("%s PLUS ONE L\n", dial->input);
            }
        }
        
        else if (direction[0] == 'R'){
            dial->dialValue += number;
            if (dial->dialValue > dial->max){
                dial->dialValue-= (dial->max+1);
                dial->pswd+=1;
                //printf("%s PLUS ONE R\n", dial->input);
            }
        }
        printf("%sPSWD: %d\nDial: %d\n\n",dial->input,dial->pswd,dial->dialValue);
    }

        /*if (dial->dialValue == 0){
            dial->pswd+=1;
        }*/
        //printf("%d\n",number);

        /*if (dial->pswd == 22){
            printf("pswd 22");
        }*/
    return 0;
}



int readInstruction(dial_state* dial){
    while(fgets(dial->input, sizeof(dial->input),dial->fptr) != NULL){
       // printf("%s",dial->input);
        findNextValue(dial);
    }
    return 0;
}

int main (void){
    dial_state dial;
    dial.dialValue=50;
    dial.max=99;
    dial.min=0;
    dial.pswd=0;
    dial.fptr=fopen("/grmn/prj/aoem/garmin/misc/funbox/advent-of-code/day-1/input.txt","r");
    readInstruction(&dial);
    fclose(dial.fptr);
    printf("Pswd=%d",dial.pswd);
    return 0;
}