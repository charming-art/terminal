package project;

public class brickE extends basicBrick{
	  public int x,y,move,delay;
	    
	    public brickE(int x,int y){
	    	super(x,y);
	    	 
	    	for(int d=0;d<4;d++){
	    		brick[0][2][1]=value;
	    		brick[0][2][4]=value;
	    		brick[0][2][3]=value;
	    		brick[0][2][2]=value;
	    	}
	    	for(int d=1;d<=3;d++){
	    		for(int i=0;i<=4;i++){
	    			for(int j=0;j<=4;j++){
	    				brick[d][i][j]=brick[d-1][4-j][i];
	    			}
	    		}
	    	}
	    }

}
