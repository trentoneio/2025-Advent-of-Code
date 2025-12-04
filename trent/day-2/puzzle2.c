#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char inputString[100];
    long long rangeStart;
    long long rangeEnd;
    long long invalid[1024];
    long long numInvalids;
    struct node* next;
} node;

node* create_node(){
    node* newNode = (node *)malloc(sizeof(node));
    newNode->next = NULL;
    return newNode;
}

/*long long get_values(char* inputString){
    if (sscanf(inputString, "%lld-%lld",,) == 2){
    }
    else {
        printf("ERROR FINDING RANGE");
    }


}*/

node* read_lines(FILE* fptr){
    char tmp_buf[100];
    node* head = NULL;
    node* newNode = NULL;
    node* oldNode = NULL;

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

long long get_ranges(node* head){
    node* curNode = head;
    long long start, end;
    while (curNode != NULL){
        if(sscanf(curNode->inputString, "%lld-%lld",&start,&end) == 2){
            curNode->rangeStart = start;
            curNode->rangeEnd = end;
            curNode = curNode->next;
        }
    }
    return 0;
}

long long split_string(char* inputString, char* str1, char* str2){
    long long len = strlen(inputString);
    long long len1 = len/2;
    long long len2 = len - len1;
    memcpy(str1, inputString,len1);
    str1[len1]='\0';
    memcpy(str2, inputString+len1,len2);
    str2[len2]='\0';
    // printf("split_string input: %s\tstr1: %s\tstr2: %s\n", inputString, str1, str2);
    return 0;
}

long long handle_invalids(node* head, long long * invalidSize){
    node* curNode = head;
    while (curNode != NULL){
        for(long long i = curNode->rangeStart; i <= curNode->rangeEnd; i++){
            char tmp_buf[100];
            sprintf(tmp_buf,"%lld",i);
            char str1[100];
            char str2[100];
            split_string(tmp_buf, str1, str2);
            // printf("handle_invalids str1: %s\tstr2: %s\n", str1, str2);
            if (strcmp (str1, str2) == 0 ){
                curNode->invalid[*invalidSize] = i;
                (*invalidSize)++;
            }

        }
    curNode->numInvalids=*invalidSize;    
    curNode = curNode->next;
    *invalidSize=0;
    }
    return 0;
}

long long add_invalids(node* head, long long* sum){
    node* curNode = head;
    while (curNode != NULL){
        for(long long i = 0; i < curNode->numInvalids; i++){
            (*sum)+=curNode->invalid[i];
            printf("\n");
            printf("sum:%lld\n",*sum);
        }
        /*if(curNode->rangeStart == 439729){
            printf("STOP");
        }*/
        curNode = curNode->next;

    }
    return 0;
}


long long output_ll_data(node* head){
    node* curNode = head;
    long long cnt = 1;
    printf("OUTPUTTING DATA FROM LINKED LIST\n");
    while (curNode != NULL){
        printf("Node #%lld:\trangeStart: %lld\trangeEnd: %lld\tnumInvalids: %lld\tinputString: %s", cnt, curNode->rangeStart, curNode->rangeEnd, curNode->numInvalids, curNode->inputString);
        cnt++;
        curNode = curNode->next;
    }
    return 0;
}


long long main (void){
    long long sum = 0;
    FILE* fptr= fopen("/grmn/prj/aoem/garmin/misc/funbox/advent-of-code/day-2/input.txt","r");
    node* head = read_lines(fptr);
    get_ranges(head);
    long long invalidSize = 0;
    handle_invalids(head, &invalidSize);
    output_ll_data(head);
    add_invalids(head,&sum);
    fclose(fptr);
}