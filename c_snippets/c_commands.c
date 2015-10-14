#include <sys/stat.h> 
#include <sys/types.h> 
#include <fcntl.h>
#include <unistd.h>
#include <dirent.h>
#include <stdio.h>
#include <errno.h>

int makeDirectory(const char *path, mode_t mode)
{
	if(mkdir(path, mode) != 0){
		perror("mkdir error"); 
	}else{
		return 0;	
	}
	return -1; 
}

int CreateNewFile(const char *name)
{
	int fds = open(name, O_CREAT);
	if(fds == -1){
		perror("open error");
		return -1; 
	}
	else{
	    // read or write here
	    close(fds);
	}
	
	return 0;
}

int makeSoftLink(const char *oldPath, const char *newPath)
{
	if (symlink(oldPath, newPath) != 0)
		perror("connot create softLink");
	return 0; 
}

int createHardLink(const char *oldPath, const char *newPath)
{
	if (symlink(oldPath, newPath) != 0)
		perror("connot create hardLink");
	return 0; 
}

int getCurrentDirectory()
{
	char buff[1024];
	char *cwd = getcwd (buff, 1024);
	if (cwd == NULL)
	perror("getcwd error");
	else
	printf("cwd is %s\n", buff);
	return 0;
}

int listFiles(const char *directoryName){
	struct dirent *entry;
	DIR *dir = opendir(directoryName);
	errno = 0;
	while ((entry = readdir (dir)) != NULL) {
	printf("%s\n", entry->d_name);
	}
	if(errno && !entry)
	perror ("readdir");
	closedir (dir);
	return 0; 
}

int showAttributes(const char *fileName)
{
	struct stat info;
	if (stat (fileName, &info) != 0){
		perror("stat error reason:");
	}else{
		printf("The stat for file test.txt:\n");
		printf(" inode : %lld \n", (long long) info.st_ino);
		printf(" dev : %ld\n", (long) info.st_dev);
		printf(" rdev : %ld\n", (long) info.st_rdev);
		printf(" access: %lo \n", info.st_mode & ACCESSPERMS );
		printf(" links : %ld\n", (long) info.st_nlink);
		printf(" uid : %ld\n", (long) info.st_uid);
		printf(" gid : %ld\n", (long) info.st_gid);
	}
	return 0;
}

int changeFilePermissions(const char *fileName, mode_t mode)
{
	int err = chmod(fileName, mode);
	if (err != 0)
		perror("chmod error");
	return 0;
}

int removeDirectory(const char *directoryName)
{
	return rmdir(directoryName);
}

int renameFile(const char *oldpath, const char *newpath)
{
	if(rename(oldpath, newpath) != 0)
		perror("rename error");
		
	return 0;
}

int writeToFile(const char *name, const char  *buffer, int length)
{
	int fds = open(name, O_RDWR |O_CREAT, S_IXUSR); 
	
	if(fds == -1){ 
		perror("open error"); 
	} 
	else{ 
		int status = write(fds, buffer, length); 
 
		if(status == -1) 
			perror("write error"); 
 
		close(fds); 
	}
}

int readFromFile(const char *file)
{
	char buff[255]; 
	int rdStatus; 
	int fds = open(file, O_RDONLY); 
	
	if(fds == -1){ 
      perror("open error"); 
    }else{ 
		char byte; 
		int rdStatus; 
		
		while(1){ 
			rdStatus = read(fds, &byte, 1); 
			if(rdStatus == 0 || rdStatus == -1)
				break;
			
			printf("%c", byte); 
			
		} 
		printf("\n");
	}
	
	close(fds);
	
}

/* 
	Simple program to demonstrate knowledge in C programming language. 
	It was part of the course assignments that I had at my university.
*/
int main()
{
	char firstAttrib[255], secondAttrib[255], str[255];
	
	int choice = 0;
	
	while(1){
		printf("Please select one of the following:\n");
		printf("1- Create new directory\n"); 
		printf("2- Create new file\n");
		printf("3- Create softLink\n");
		printf("4- Create hardLink\n");
		printf("5- List files in a specific directory\n");
		printf("6- Show attributes for a certain file\n");
		printf("7- Get Current working directory\n");
		printf("8- Change file permissions\n");
		printf("9- Remove directory\n");
		printf("10- RenameFile\n");
		printf("11- Write to a file\n");
		printf("12- Read from a file\n");
		printf("0- quit\n");

		scanf("%i", &choice);
		printf("You selected choice %i \n", choice);
		if (choice == 0){		
			break;
		}
		
		switch(choice)
		{
			case 1 :
			printf("Please enter the name of the directory");
			scanf("%s", &firstAttrib);
			printf("Please enter Permission\n");
			scanf("%s", &secondAttrib);
			makeDirectory(firstAttrib, secondAttrib); 
			break;
			case 2 :
			printf("Please enter the name of the file\n");
			scanf("%s", &firstAttrib);
			CreateNewFile(firstAttrib);
			break;
			case 3 : 
			printf("Please enter old path\n");
			scanf("%s", &firstAttrib);
			printf("Please enter new path\n");
			scanf("%s", &secondAttrib);
			makeSoftLink(firstAttrib, secondAttrib); 
			break;
			case 4 : 
			printf("Please enter old path\n");
			scanf("%s", &firstAttrib);
			printf("Please enter new path\n");
			scanf("%s", &secondAttrib);
			createHardLink(firstAttrib, secondAttrib); 
			break;
			case 5 : 
			printf("Please enter path to directory\n");
			scanf("%s", &firstAttrib);
			listFiles(firstAttrib);
			break;
			case 6 : 
			printf("Please enter path file name\n");
			scanf("%s", &firstAttrib);
			showAttributes(firstAttrib);
			break;
			case 7 :		
			getCurrentDirectory();
			break;		
			case 8 : 
			printf("Please enter the name of the file");
			scanf("%s", &firstAttrib);
			printf("Please enter Permission\n");
			scanf("%s", &secondAttrib);
			changeFilePermissions(firstAttrib, secondAttrib); 
			break;	
			case 9 : 
			printf("Please enter the name of the directory\n");
			scanf("%s", &firstAttrib);
			removeDirectory(firstAttrib);
			case 10: 
			printf("Please enter the name of the file to rename\n");
			scanf("%s", &firstAttrib);
			printf("Please enter new name of the file\n");
			scanf("%s", &secondAttrib);
			renameFile(firstAttrib, secondAttrib);
			break;
			case 11: 
			printf("Please enter the name of the file to write to\n");
			scanf("%s", &firstAttrib);
			getchar();
			printf("Please enter what you want to write\n");
			fgets(secondAttrib, 255, stdin);
			 /* Remove trailing newline, if there. */
			if ((strlen(secondAttrib)>0) && (secondAttrib[strlen (secondAttrib) - 1] == '\n'))
				secondAttrib[strlen (secondAttrib) - 1] = '\0';
			writeToFile(firstAttrib, secondAttrib, strlen(secondAttrib));
			break;
			case 12:
			printf("Please enter the name of the file to read from\n");
			scanf("%s", &firstAttrib);
			readFromFile(firstAttrib);
			
		}
	
	}
/*
	makeDirectory("../haha", S_IRWXU);
	CreateNewFile("bla.txt");
	makeSoftLink("bla.txt","blaSoft.txt");
	createHardLink("bla.txt","blaHard.txt");	
	listFiles(".");
	showAttributes("bla.txt");
	getCurrentDirectory();
	changeFilePermissions("bla.txt", S_IXUSR);
	removeDirectory("../haha");*/
	return 0; 
}
