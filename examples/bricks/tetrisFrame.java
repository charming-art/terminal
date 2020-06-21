package project;

import javax.swing.JFrame;

public class tetrisFrame {
	public static void main(String []args){
		JFrame frame=new JFrame("TetrisGame");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		tetrisPanel panel= new tetrisPanel(27,14);
		frame.getContentPane().add(panel);
		frame.pack();
		frame.setVisible(true);
	}

}
