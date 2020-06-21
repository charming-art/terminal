package project;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;





public class tetrisPanel extends JPanel {
       public int Grid [][];
       public Color[] color={Color.white,Color.red,Color.orange ,Color.yellow,Color.green,Color.cyan,Color.blue,Color.pink,Color.black};
       public int x1=450,y1=40,x2,y2,size,Gridx,Gridy,delay=500,move;
       public Timer maintimer;
       public JButton begin;
       public int insertX;
       public ArrayList<basicBrick> bricks=new ArrayList<basicBrick>();
       public int count=0;
       public JButton restart,end;
       public JLabel score;
       public int number=0,basicnumber=10;
       public int delectN=0;
       
       public tetrisPanel(int length,int width){
    	   addKeyListener(new moveListener());
    	   setFocusable(true);
    	   begin= new JButton("开始游戏");
    	   begin.addActionListener(new start());
    	   maintimer=new Timer(delay,new main());
    	   restart= new JButton("重新开始");
    	   restart.addActionListener(new restart());
    	   end=new JButton("结束");
    	   end.addActionListener(new over());
    	   score=new JLabel("分数"+number);
    	   
    	   size=29;
    	   move=size;
    	   
    	   insertX=(int)(x1+((width-5)/2)*size);
    	   
    	   Gridx=width;Gridy=length;
    	   Grid=new int[length][width];
    	   for(int i=0;i<Gridy;i++)
    		   for(int j=0;j<Gridx;j++)
    			   Grid[i][j]=0;
    	   
    	   x2=x1+size*width;y2=y1+size*length;
    	   
    	   
    	   add(begin);
    	   add(end);
    	   add(restart);
    	   add(score);
    	   setPreferredSize(new Dimension(300,200));
		   setBackground(Color.gray);
    	  
		  
       }
       public void paintComponent(Graphics page){
    	   super.paintComponent(page);
    	   page.setColor(Color.black);
    	   page.fillRect(400, 40, 800, 1000);
    	   
    	   int Gx,Gy;
           for(int i=0;i<Gridy;i++) {
        	   Gy=y1+i*size;
        	   Gx=x1;
        	   for(int j=0;j<Gridx;j++){
        		   Gx+=size;
        		   page.setColor(color[Grid[i][j]]);
        		   page.fillRect(Gx, Gy, size, size);
        	   }
           }
           for(int i=0;i<5;i++) {
        	   Gy=y1+i*size;
        	   Gx=x1;
        	   for(int j=0;j<Gridx;j++){
        		   Gx+=size;
        		   page.setColor(Color.black);
        		   page.fillRect(Gx, Gy, size, size);
        	   }
           }
           if(!bricks.isEmpty()){
           basicBrick next=bricks.get(bricks.size()-1);
        	   int a=950,b=400;
        	   int nextX,nextY;
        	   for(int i=0;i<5;i++){
        		   nextY=b+i*size;
        		   nextX=a;
        		   for(int j=0;j<5;j++){
        			   nextX +=size;
        		   page.setColor(color[next.brick[next.mode][i][j]]);
        		   page.fillRect(nextX, nextY, size, size);}
        	   }
           }  
       }

         public class main implements ActionListener{
        	 public void actionPerformed(ActionEvent event){
        		basicBrick last;
        		 if(bricks.isEmpty()){
        			 bricks.add(getNew());
        			 bricks.add(getNew());
        			 print(bricks.get(0));
        			 repaint();
        		 }
        		 else{  
        			 last=bricks.get(bricks.size()-2);
        			 delet(last);
        			 if(valid(last.x,last.y+size,last)){
        				 last.y +=size;
        				 print(last);
        			 }
        			 else{
        				 
        				 print(last);
        				 delectfull(last);
        				 if(over(last)){
        					 maintimer.stop();
        					 begin.setText("游戏结束");}
        				 bricks.add(getNew());
        				 print(bricks.get(bricks.size()-2));
        			 }
        			 
        			 repaint();
        		 }
      		 }	 
         }
  		 
         public class start implements ActionListener{
        	 public void actionPerformed(ActionEvent event){
        		 count++;
        		 if(count%2==1){
        	     begin.setText("暂停");
      			 maintimer.start();
      			 repaint();
      			 tetrisPanel.this.requestFocus();}
        		 else{
        			 begin.setText("继续");
        			 maintimer.stop();
        			 repaint();
        			 tetrisPanel.this.requestFocus();
        		 }
      		 }	 
         }
  		
         public void print(basicBrick jim){
        	 int a=(jim.x-x1)/size;
        	 int b=(jim.y-y1)/size;
        	 for(int i=0;i<5;i++)
        		 for(int j=0;j<5;j++){
        			 if(in(i+b,j+a)){
        				Grid[i+b][j+a] +=jim.brick[jim.mode][i][j];
        			 }
        		 }
        	
        	 
         }
         
         public void delet(basicBrick jim){
        	 int a=(jim.x-x1)/size;
        	 int b=(jim.y-y1)/size;
        	 for(int i=0;i<5;i++)
        		 for(int j=0;j<5;j++){
        			 if(in(i+b,a+j)){
        				if(jim.brick[jim.mode][i][j] !=0)
        					Grid[i+b][j+a]=0;	
        			 }
        		 }
        	
         }
         
         public boolean valid(int x,int y,basicBrick jim){
        	 boolean result=true;
        	 int a=(x-x1)/size;
        	 int b=(y-y1)/size;
        	 for(int i=0;i<5;i++)
        		 for(int j=0;j<5;j++){
        			 if(jim.brick[jim.mode][i][j] !=0){
        				 if(!in(i+b,a+j) || (Grid[i+b][a+j]!=0))
        					 result=false;
        			 }
        			 
        		 }
        	 return result;
         }
         public boolean in(int x ,int y){
        	 boolean result=true;
        	 if(x<0 || x>=Gridy  || y<0  || y>=Gridx)
        		 result=false;
        	 return result;
         }
       
       
       
         public class moveListener implements KeyListener{
         	public void keyPressed(KeyEvent event){
         		basicBrick jim=bricks.get(bricks.size()-2);
         	
         		switch(event.getKeyCode()){
         		case KeyEvent.VK_UP:{
         			delet(jim);
         			
         			jim.mode=(jim.mode+1)%4;
         			if(valid(jim.x,jim.y,jim))
         			print(jim);
         			else{
         				jim.mode--;
         				if(jim.mode<0)
         					jim.mode+=4;
         				else jim.mode %= 4;
         				print(jim);
         			}
         		}
         			
         			break;
         		case KeyEvent.VK_DOWN:
         			delet(jim);
         			if(valid(jim.x,jim.y+size,jim)){
         				jim.y +=size;
         				print(jim);
         			}
         			else print(jim);
         		
         		
         			break;
         		case KeyEvent.VK_LEFT:
         			delet(jim);
         			if(valid(jim.x-size,jim.y,jim)){
         				jim.x -=size;
         				print(jim);
         			}
         			else print(jim);
         		
         			
         			break;
         		case KeyEvent.VK_RIGHT:
         			delet(jim);
         			if(valid(jim.x+size,jim.y,jim)){
         				jim.x +=size;
         				print(jim);
         			}
         			else print(jim);
         		
         			
         			break;
         		case KeyEvent.VK_SPACE:
         			boolean kim=true;
         			while(kim){
         				delet(jim);
             			if(valid(jim.x,jim.y+size,jim)){
             				jim.y +=size;
             				print(jim);
             			}
             			else {print(jim);
             			kim=false;}
         				}
         			break;
         			}
         		
         		repaint();
         		
         	}
         	public void keyTyped(KeyEvent event){}
         	public void keyReleased(KeyEvent event){}
         }
       
       public void delectfull(basicBrick jim){
    	   boolean isfull=true;
    	   int b=(jim.y-y1)/size;
    	   delectN=0;
    	   for(int j=b;j<b+5;j++){
    		   isfull=true;
    		   for(int i=0;i<Gridx;i++){
    			   if(j>=0 && j<Gridy){
    				   if(Grid[j][i] ==0)
    					   isfull=false;
    			   }
    			   else isfull=false;
    		   }
    		   if(isfull){
    			   delectN++;
    			   deletfull(j);
    			  
    				if(number==50)
    					delay-=50;
    				if(number==100)
    					delay-=50;
    				if(number==200)
    					delay-=50;
    				if(number==400)
    					delay-=50;}
    	   }
    	   if(delectN==1)
    		   number += basicnumber;
    	   if(delectN==2)
    		   number += basicnumber*3;
    	   if(delectN==3)
    		   number += basicnumber*6;
    	   if(delectN==4)
    		   number += basicnumber*10;
			score.setText("分数"+number);
       }
       
       public void deletfull(int line){
    	   for(int j=line;j>0;j--){
    		   for(int i=0;i<Gridx;i++){
    			   Grid[j][i]=Grid[j-1][i];
    		   }
    	   }
    	   for(int i=0;i<Gridx;i++){
    		   Grid[0][i]=0;
    	   }
       }
       
       
      public basicBrick getNew(){
    	  int x=(int)(Math.random()*7);
    	  if(x==0)
    		  return new brickA(insertX,y1);
    	  if(x==1)
    		  return new brickB(insertX,y1);
    	  if(x==2)
    		  return new brickC(insertX,y1);
    	  if(x==3)
    		  return new brickD(insertX,y1);
    	  
    	  if(x==4)
    		  return new brickE(insertX,y1);
    	  if(x==5)
    		  return new brickF(insertX,y1);
    	  
    	  if(x==6)
    		  return new brickG(insertX,y1);
    	  return new brickA(insertX,y1);
    	  
    	  
    	  
    	  
      }
      
      public class restart implements ActionListener{
     	 public void actionPerformed(ActionEvent event){
     		 if(!maintimer.isRunning()){
     			for(int i=0;i<Gridy;i++)
         		   for(int j=0;j<Gridx;j++)
         			   Grid[i][j]=0;
     			bricks.clear();
     			begin.setText("开始游戏");
     			count++;
     			number=0;
     			score.setText("分数"+number);
     			repaint();
     			 
     		 }
     		 
     	 }
      }
      public class over implements ActionListener{
      	 public void actionPerformed(ActionEvent event){
      		 if(maintimer.isRunning())
      			 maintimer.stop();
      		 
      	 }
       }
      
      public boolean over(basicBrick jim){
    	  boolean result=false;
    	 
     	 int a=(jim.x-x1)/size;
     	 int b=(jim.y-y1)/size;
     	 for(int i=0;i<5;i++)
     		 for(int j=0;j<5;j++){
     			 if(jim.brick[jim.mode][i][j] !=0){
     				 if((i+b)<5)
     					 result=true;
     			 }
     			 
     		 }
     	 return result;
      }
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
}
