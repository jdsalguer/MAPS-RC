#include <iostream>
#include <stdio.h>
#include <stdlib.h> // <-- adds exit for part 2
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <string>
using namespace std;


class JSON
{
private:

public:
	string message;
	string jhead;
	string jbody;
	string jfoot;
	string jpid;
	JSON() {
		int pid = getpid();
		jpid = to_string(pid);
	}

	void status(string s){jhead=s; parse();}
	void body(string s){jbody=s; parse();}
	void foot(string s){jfoot=s; parse();}

	void parse() {
		message = "{ " + asJSON("status",jhead) + " , ";
		message += asJSON("body",jbody) + " , ";
		message += asJSON("foot",jfoot) + " , ";
		message += asJSON("pid",jpid) + " } ";
	}
	void reset() {
		message = "";
		jhead="";
		jbody="";
		jfoot="";
	}
	string asJSON(string s1, string s2)
	{
		return "\"" + s1 + "\":\"" + s2 + "\"";
	}

	friend ostream& operator<<(ostream& os, const JSON& json);
};
ostream& operator<<(ostream& os, const JSON& json) {
	os << json.message << endl;
	return os;
}

int main(int argc, char const *argv[])
{
	int parent = getpid();
	JSON msg;
	string s;

//	sleep();
	msg.status("GOOD");
	msg.body("my_state_information");
	msg.foot("more_parameters");
	cout << msg;
	msg.reset();

	int i=0;
	while(s != "exit")
	{
		msg.reset();
		msg.status("WAITING");
		msg.body("waiting_for_input");
		msg.foot("exit_will_end_process");
		cout << msg;
		msg.reset();

		cin >> s;
		//sleep(1);
		if(s == "exit") break;
		else if(i++ == 4) break;
		s.clear();
	}
	s.clear();
	msg.status("STOP");
	msg.body("new_state");
	msg.foot("more_parameters...");
	cout << msg;

	return 0;
}