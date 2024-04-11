using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace teste
{
    public partial class Frm_Exercicio : Form
    {
        public Frm_Exercicio()
        {
            InitializeComponent();
        }

        private void Btn_Search_Click(object sender, EventArgs e)
        {
            OpenFileDialog of = new OpenFileDialog();
            of.InitialDirectory = "C:\\Users\\carva\\Downloads";
            
            if (DialogResult.OK == of.ShowDialog())
            {
                var arquivo = of.FileName;
                //string[] lines = File.ReadAllLines(arquivo);
                var lines = File.ReadAllLines(arquivo);
                foreach (var line in lines)
                {
                    var words = line.Split('a','e','i','o','u');

                    //Txt_Resultado.Text = line + "\t";
                    //Txt_Resultado.Text = words[0] + "\t\r\n";
                   // Txt_Resultado.AppendText( line + "\t\r\n");
                    //Txt_Resultado.AppendText( words[1] + "\t\r\n");
                  //  Txt_Resultado.AppendText(words.Length.ToString() + "\t\r\n");
                    if(words.Length > 6)
                    {
                        Txt_Resultado.AppendText(line + "\t\r\n");

                    }
                }
                    
                //for (int i = 0; i< lines.Length; i++)
                //{
                //    Txt_Resultado.Text = i + "\r\n";
                //}
            }
            //of.ShowDialog();
        }
    }
}
