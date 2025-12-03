#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char inputString[102];
    long long maxJoltage;
    struct battery* next;
} battery;

battery* create_node(){
    battery* newNode = (battery *)malloc(sizeof(battery));
    newNode->next = NULL;
    return newNode;
}

battery* read_lines(FILE* fptr){
    char tmp_buf[102];
    battery* head = NULL;
    battery* newNode = NULL;
    battery* oldNode = NULL;

    while(fgets(tmp_buf, sizeof(tmp_buf),fptr) != NULL){
        // printf("%s",tmp_buf);
        newNode = create_node();
        strcpy(newNode->inputString,tmp_buf);

        if (head == NULL){
            head = newNode;
        }

        if (oldNode != NULL){
            oldNode->next = newNode;
        }

        oldNode = newNode;
    }

    return head;
}

int find_max(battery* head,int strLength){
    battery* curNode = head;
    while (curNode != NULL){
    
    char firstDigit = '0';
    int firstDigitIdx = -1;

    char secondDigit = '0';
    int secondDigitIdx = -1;

    char thirdDigit = '0';
    int thirdDigitIdx = -1;

    char fourthDigit = '0';
    int fourthDigitIdx = -1;

    char fifthDigit = '0';
    int fifthDigitIdx = -1;

    char sixthDigit = '0';
    int sixthDigitIdx = -1;

    char seventhDigit = '0';
    int seventhDigitIdx = -1;

    char eighthDigit = '0';
    int eighthDigitIdx = -1;

    char ninthDigit = '0';
    int ninthDigitIdx = -1;

    char tenthDigit = '0';
    int tenthDigitIdx = -1;

    char eleventhDigit = '0';
    int eleventhDigitIdx = -1;

    char twelfthDigit = '0';
    int twelfthDigitIdx = -1;
        // 1
        for (int i=0;i<(strLength-11);i++){
            if (curNode->inputString[i] > firstDigit){
                firstDigit = curNode->inputString[i];
                firstDigitIdx = i;
            }
        }
        // 2
        for (int i=(firstDigitIdx+1);i<strLength && i<(strLength-10);i++){
            if (curNode->inputString[i] > secondDigit){
                secondDigit = curNode->inputString[i];
                secondDigitIdx = i;
            }
        }
        // 3
        for (int i=(secondDigitIdx+1);i<strLength && i<(strLength-9);i++){
            if (curNode->inputString[i] > thirdDigit){
                thirdDigit = curNode->inputString[i];
                thirdDigitIdx = i;
            }
        }
        // 4
        for (int i=(thirdDigitIdx+1);i<strLength && i<(strLength-8);i++){
            if (curNode->inputString[i] > fourthDigit){
                fourthDigit = curNode->inputString[i];
                fourthDigitIdx = i;
            }
        }
        // 5
        for (int i=(fourthDigitIdx+1);i<strLength && i<(strLength-7);i++){
            if (curNode->inputString[i] > fifthDigit){
                fifthDigit = curNode->inputString[i];
                fifthDigitIdx = i;
            }
        }
        // 6
        for (int i=(fifthDigitIdx+1);i<strLength && i<(strLength-6);i++){
            if (curNode->inputString[i] > sixthDigit){
                sixthDigit = curNode->inputString[i];
                sixthDigitIdx = i;
            }
        }
        // 7
        for (int i=(sixthDigitIdx+1);i<strLength && i<(strLength-5);i++){
            if (curNode->inputString[i] > seventhDigit){
                seventhDigit = curNode->inputString[i];
                seventhDigitIdx = i;
            }
        }
        // 8
        for (int i=(seventhDigitIdx+1);i<strLength && i<(strLength-4);i++){
            if (curNode->inputString[i] > eighthDigit){
                eighthDigit = curNode->inputString[i];
                eighthDigitIdx = i;
            }
        }
        // 9
        for (int i=(eighthDigitIdx+1);i<strLength && i<(strLength-3);i++){
            if (curNode->inputString[i] > ninthDigit){
                ninthDigit = curNode->inputString[i];
                ninthDigitIdx = i;
            }
        }
        // 10
        for (int i=(ninthDigitIdx+1);i<strLength && i<(strLength-2);i++){
            if (curNode->inputString[i] > tenthDigit){
                tenthDigit = curNode->inputString[i];
                tenthDigitIdx = i;
            }
        }
        // 11
        for (int i=(tenthDigitIdx+1);i<strLength && i<(strLength-1);i++){
            if (curNode->inputString[i] > eleventhDigit){
                eleventhDigit = curNode->inputString[i];
                eleventhDigitIdx = i;
            }
        }
        // 12
        for (int i=(eleventhDigitIdx+1);i<strLength;i++){
            if (curNode->inputString[i] > twelfthDigit){
                twelfthDigit = curNode->inputString[i];
                twelfthDigitIdx = i;
            }
        }
        curNode->maxJoltage = (((long long)firstDigit-48)*100000000000) + (((long long)secondDigit-48)*10000000000) + (((long long)thirdDigit-48)*1000000000) + (((long long)fourthDigit-48)*100000000) + (((long long)fifthDigit-48)*10000000) + (((long long)sixthDigit-48)*1000000) + (((long long)seventhDigit-48)*100000) + (((long long)eighthDigit-48)*10000) + (((long long)ninthDigit-48)*1000) + (((long long)tenthDigit-48)*100) + (((long long)eleventhDigit-48)*10) + ((long long)twelfthDigit-48);
        printf("firstDigit: %d\tsecondDigit:%d\tmaxJoltage: %lld\tinputString: %s\n", ((int)firstDigit-48), ((int)secondDigit-48), curNode->maxJoltage, curNode->inputString);
        curNode = curNode->next;
    }
}

int add_joltages(battery* head, long long* sum){
    battery* curNode = head;
    while (curNode != NULL){
        (*sum)+=curNode->maxJoltage;
        printf("sum:%lld\n",*sum);
        /*if(curNode->rangeStart == 439729){
            printf("STOP");
        }*/
        curNode = curNode->next;

    }
    return 0;
}


int main (void){
    long long sum = 0;
    int strLength = 100;
    FILE* fptr= fopen("/grmn/prj/aoem/garmin/misc/funbox/advent-of-code/day-3/input.txt","r");
    battery* head = read_lines(fptr);
    find_max(head, strLength);
    add_joltages(head, &sum);
    return 0;
}