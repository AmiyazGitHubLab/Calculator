#include <iostream>
#include <vector>
#include <map>
#include <math.h>

using namespace std;
int getLargestIntVector(vector<int> useVector){
    int largest = 0;
    for(int i = 0; i < useVector.size(); i++){
        if(useVector[i] > largest) largest = useVector[i];
    }
    return largest;
}
string input(string msg=""){
    cout<<msg;
    string value;
    getline(cin, value);
    return value;
}
int fact(int n){
    if(n == 0) return 0;
    int j = 1;
    for(int i = 1; i < n; i++) j*=i+1;
    return j;
}
void outputVectorString(vector<string> vectorToOut){
    cout<<"[";
    if(vectorToOut.size()!=0){
        for(int i = 0; i<vectorToOut.size(); i++) {
            cout<<"'"<<vectorToOut[i]<<"'";
            if(i!=vectorToOut.size()-1){
                cout<<", ";
            }
        }
    }
    cout << "]" << endl;
}

void outputVectorChar(vector<char> vectorToOut){
    cout<<"[";
    if(vectorToOut.size()!=0){
        for(int i = 0; i<vectorToOut.size(); i++) {
            cout<<"'"<<vectorToOut[i]<<"'";
            if(i!=vectorToOut.size()-1){
                cout<<", ";
            }
        }
    }
    cout << "]" << endl;
}

vector<char> stringToCharVector(string s){
    vector<char> returnVector;
    for(int i = 0; i < s.length(); i++){
        returnVector.push_back(s[i]);
    }
    return returnVector;
}

void outputVectorInt(vector<int> vectorToOut){
    cout<<"[";
    if(vectorToOut.size()!=0){
        for(int i = 0; i<vectorToOut.size(); i++) {
            cout<<vectorToOut[i];
            if(i!=vectorToOut.size()-1){
                cout<<", ";
            }
        }
    }
    cout << "]" << endl;
}
void outputMapII(map<int,int> input){
    cout<<"{";
    int index = 0;
    for(auto const& elem : input){
        cout << elem.first << ": " << elem.second;
        if(index!=input.size()-1){
            cout<<", ";
        }
        index++;
    }
    cout<<"}"<<endl;
}
bool is_integer(float check){
    return check-floorf(check) == 0;
}
int main()
{
    bool verbose = false;
    vector<char> value;
    while(true){
        value = stringToCharVector(input("> "));
        if(verbose) outputVectorChar(value);
        int pointer = 0;
        vector<string> parsed;
        string join = "";
        // Parsing start
        while(true){
            char workingValue = value[pointer];
            pointer++;
            if(workingValue == ' ') continue;
            bool isNumber=isdigit(workingValue)||workingValue=='.';
            if(!isNumber){
                if(join.length() != 0){
                    parsed.push_back(join);
                    if(verbose){
                        outputVectorString(parsed);
                    }
                    join = "";
                }
                parsed.push_back(string(1,workingValue));
                if(workingValue == '!'){
                    if(verbose){
                        outputVectorString(parsed);
                    }
                    parsed.push_back("");
                }
                if(verbose){
                    outputVectorString(parsed);
                }
            }else{
                join += workingValue;
            }
            if(pointer==value.size()){
                if(join.length()!=0){
                    parsed.push_back(join);
                }
                if(verbose) outputVectorString(parsed);
                break;
            }
        }
        /*
        Parsing end
        Lexing start
        */
        vector<string> lexTree = parsed;
        vector<int> priorities;
        pointer = 0;
        while(true){
            string reading = lexTree[pointer];
            if(reading == "^" || reading == "!"){
                priorities.push_back(pointer);
                if(verbose) outputVectorInt(priorities);
            }
            pointer++;
            if(pointer == parsed.size()-1) break;
        }
        pointer = 0;
        while(true){
            string reading = lexTree[pointer];
            if(reading == "*" || reading == "/"){
                priorities.push_back(pointer);
                if(verbose) outputVectorInt(priorities);
            }
            pointer++;
            if(pointer == parsed.size()-1) break;
        }
        pointer = 0;
        while(true){
            string reading = lexTree[pointer];
            if(reading == "+" || reading == "-"){
                priorities.push_back(pointer);
                if(verbose) outputVectorInt(priorities);
            }
            pointer++;
            if(pointer == parsed.size()-1) break;
        }
        /*
            Lexing end
            Calculating start
        */
        map<int,int> alloffsets;
        for(int i = 0; i < getLargestIntVector(priorities)+1; i++){
            alloffsets.insert(pair<int,int>(i,0));
        }
        pointer = 0;
        int offset = 0;
        int location = 0;
        if(parsed.size()==1) location=priorities[pointer];
        if(verbose) outputVectorString(lexTree);

        while(true){
            if(parsed.size()==0) break;

            location = priorities[pointer];
            if(verbose) outputMapII(alloffsets);
            for(int i =0; i < location; i++){
                if(alloffsets[i]<location){
                    location-=alloffsets[i];
                }
            }
            char operation=lexTree[location][0];
            switch(operation){
                case '!': {
                    string first = lexTree[location-1];
                    lexTree.erase(lexTree.begin() + location + 1);
                    lexTree.erase(lexTree.begin() + location);
                    lexTree.erase(lexTree.begin() + location - 1);
                    lexTree.insert(lexTree.begin() + location - 1, to_string(fact(stoi(first))));
                    alloffsets[location]=alloffsets[location]+2;
                    break;
                }
                case '^': {
                    string first = lexTree[location-1];
                    string second = lexTree[location+1];
                    lexTree.erase(lexTree.begin() + location + 1);
                    lexTree.erase(lexTree.begin() + location);
                    lexTree.erase(lexTree.begin() + location - 1);
                    lexTree.insert(lexTree.begin() + location - 1, to_string(pow(stof(first),stof(second))));
                    alloffsets[location]=alloffsets[location]+2;
                    break;
                }
                case '/': {
                    string first = lexTree[location-1];
                    string second = lexTree[location+1];
                    lexTree.erase(lexTree.begin() + location + 1);
                    lexTree.erase(lexTree.begin() + location);
                    lexTree.erase(lexTree.begin() + location - 1);
                    lexTree.insert(lexTree.begin() + location - 1, to_string(stof(first) / stof(second)));
                    alloffsets[location]=alloffsets[location]+2;
                    break;
                }
                case '*': {
                    string first = lexTree[location-1];
                    string second = lexTree[location+1];
                    lexTree.erase(lexTree.begin() + location + 1);
                    lexTree.erase(lexTree.begin() + location);
                    lexTree.erase(lexTree.begin() + location - 1);
                    lexTree.insert(lexTree.begin() + location - 1, to_string(stof(first) * stof(second)));
                    alloffsets[location]=alloffsets[location]+2;
                    break;
                }
                case '-': {
                    string first = lexTree[location-1];
                    string second = lexTree[location+1];
                    lexTree.erase(lexTree.begin() + location + 1);
                    lexTree.erase(lexTree.begin() + location);
                    lexTree.erase(lexTree.begin() + location - 1);
                    lexTree.insert(lexTree.begin() + location - 1, to_string(stof(first) - stof(second)));
                    alloffsets[location]=alloffsets[location]+2;
                    break;
                }
                case '+': {
                    string first = lexTree[location-1];
                    string second = lexTree[location+1];
                    lexTree.erase(lexTree.begin() + location + 1);
                    lexTree.erase(lexTree.begin() + location);
                    lexTree.erase(lexTree.begin() + location - 1);
                    lexTree.insert(lexTree.begin() + location - 1, to_string(stof(first) + stof(second)));
                    alloffsets[location]=alloffsets[location]+2;
                    break;
                }
            }
            pointer++;
            if(verbose) outputVectorString(lexTree);
            if(pointer==priorities.size()) break;
        }
        if(is_integer(stof(lexTree[0]))){
            cout<<int(stof(lexTree[0]));
        }else{
            cout<<stof(lexTree[0]);
        }
        cout<<endl;
    }
    return 0;
}
