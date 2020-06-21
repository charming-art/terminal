package project;

public class basicBrick {
	protected int x,y,value,max=7,mode;
	protected int brick [][][]=new int [4][5][5];
	
	
	 public basicBrick(int x,int y){
		 value=(int)(Math.random()*max)+1;
		 mode=(int)(Math.random()*4);
		 this.y=y;
		 this.x=x;
		 for(int d=0;d<4;d++)
			 for(int i=0;i<5;i++)
				 for(int j=0;j<5;j++)
					 brick[d][i][j]=0;
	 }
	
	

}
