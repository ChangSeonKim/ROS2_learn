#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <termios.h>
#include <sys/ioctl.h>
int main_menu(void);
//------------------------------------------------------------------------
// 설 명 : 어플리케이션 처리
// 매 계 : 명령행 매계변수
// 반 환 : 없음
// 주 의 :
//------------------------------------------------------------------------
int main( int argc, char **argv )
{
    int     handle;
    struct  termios  oldtio,newtio;
    char    *TitleMessage = "Welcome Serial Port\r\n";
    char    Buff[256];
    int     RxCount;
    int     loop;
    int     ending;
    int key;
     // 화일을 연다.
    //handle = open( "/dev/ttyTHS2", O_RDWR | O_NOCTTY );
    handle = open( "/dev/ttyACM0", O_RDWR | O_NOCTTY );
    if( handle < 0 )
    {
        //화일 열기 실패
        printf( "Serial Open Fail [/dev/ttyACM0]\r\n "  );
        exit(0);
    }
    tcgetattr( handle, &oldtio );  // 현재 설정을 oldtio에 저장
    memset( &newtio, 0, sizeof(newtio) );
    newtio.c_cflag = B115200 | CS8 | CLOCAL | CREAD ;
    newtio.c_iflag = IGNPAR;
    newtio.c_oflag = 0;
    //set input mode (non-canonical, no echo,.....)
    newtio.c_lflag = 0;
    newtio.c_cc[VTIME] = 128;    // time-out 값으로 사용된다. time-out 값은 TIME*0.1초 이다.
    newtio.c_cc[VMIN]  = 0;     // MIN은 read가 리턴되기 위한 최소한의 문자 개수
    tcflush( handle, TCIFLUSH );
    tcsetattr( handle, TCSANOW, &newtio );
    // 타이틀 메세지를 표출한다.
    write( handle, TitleMessage, strlen( TitleMessage ) );
    // 1 문자씩 받아서 되돌린다.
    ending = 0;
    while((key=main_menu()) != 0)
    {
        switch(key)
        {
           case '1':
               printf("1 \n");
               Buff[0] = '1';
               write( handle, Buff, 1 );
               break;
           case '2':
               printf("2 \n");
               Buff[0] = '2';
               write( handle, Buff, 1 );
               break;
           case '3':
               printf("3\n");
               Buff[0] = '3';
               write( handle, Buff, 1 );
               break;
           case '4':
               printf("4\n");
               Buff[0] = '4';
               write( handle, Buff, 1 );
               break;
           case '5':
               printf("5\n");
               Buff[0] = '5';
               write( handle, Buff, 1 );
               break;
           case '6':
               printf("No.6\n");
               Buff[0] = '6';
               write( handle, Buff, 1 );
               break;
           case '7':
               printf("No.7\n");
               Buff[0] = '7';
               write( handle, Buff, 1 );
               break;
           case '8':
               printf("No.8\n");
               Buff[0] = '8';
               write( handle, Buff, 1 );
               break;
           case '9':
               printf("No.9\n");
               break;
           case '0':
               printf("No.0\n");
               break;
           case 'q':
               printf("exit\n");
               tcsetattr( handle, TCSANOW, &oldtio ); // 이전 상태로 되돌린다.
               close( handle );   // 화일을 닫는다.
               exit(0);
               break;
           default :
               printf("Wrong key ..... try again\n");
               break;
        }
    }
    tcsetattr( handle, TCSANOW, &oldtio ); // 이전 상태로 되돌린다.
    close( handle );   // 화일을 닫는다.
    return 0;
}
int getch(void)
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr( STDIN_FILENO, &oldattr );
    newattr = oldattr;
    newattr.c_lflag &= ~( ICANON | ECHO );
    tcsetattr( STDIN_FILENO, TCSANOW, &newattr );
    ch = getchar();
    tcsetattr( STDIN_FILENO, TCSANOW, &oldattr );
    return ch;
}
int main_menu(void)
{
    int key;
    printf("\n\n");
    printf("-------------------------------------------------\n");
    printf("                    MAIN MENU\n");
    printf("-------------------------------------------------\n");
    printf(" 1. LED1 off-on                 \n");
    printf(" 2. LED2 off-on                 \n");
    printf(" 3. LED3 off-on                 \n");
    printf(" 4. LED4 off-on                 \n");
    printf(" 5. ALL LED OFF                 \n");
    printf(" 6. ALL LED ON                  \n");
    printf(" 7. LED 1 2 3 4 off-on                  \n");
    printf(" 8. LED 4 3 2 1 off-on                  \n");
    printf("-------------------------------------------------\n");
    printf(" q. Motor Control application QUIT                 \n");
    printf("-------------------------------------------------\n");
    printf("\n\n");
    printf("SELECT THE COMMAND NUMBER : ");
    key=getch();
    return key;
}
