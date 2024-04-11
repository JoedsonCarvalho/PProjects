namespace teste
{
    partial class Frm_Exercicio
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Lbl_SelecaoDeArquivo = new System.Windows.Forms.Label();
            this.Btn_Search = new System.Windows.Forms.Button();
            this.Txt_Resultado = new System.Windows.Forms.TextBox();
            this.Lbl_text = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Lbl_SelecaoDeArquivo
            // 
            this.Lbl_SelecaoDeArquivo.AutoSize = true;
            this.Lbl_SelecaoDeArquivo.Font = new System.Drawing.Font("Garamond", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.Lbl_SelecaoDeArquivo.Location = new System.Drawing.Point(26, 22);
            this.Lbl_SelecaoDeArquivo.Name = "Lbl_SelecaoDeArquivo";
            this.Lbl_SelecaoDeArquivo.Size = new System.Drawing.Size(535, 34);
            this.Lbl_SelecaoDeArquivo.TabIndex = 0;
            this.Lbl_SelecaoDeArquivo.Text = "Aperte o botão pra selecionar os arquivo ";
            // 
            // Btn_Search
            // 
            this.Btn_Search.Font = new System.Drawing.Font("Garamond", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.Btn_Search.Location = new System.Drawing.Point(467, 100);
            this.Btn_Search.Name = "Btn_Search";
            this.Btn_Search.Size = new System.Drawing.Size(94, 29);
            this.Btn_Search.TabIndex = 1;
            this.Btn_Search.Text = "Search";
            this.Btn_Search.UseVisualStyleBackColor = true;
            this.Btn_Search.Click += new System.EventHandler(this.Btn_Search_Click);
            // 
            // Txt_Resultado
            // 
            this.Txt_Resultado.Location = new System.Drawing.Point(26, 177);
            this.Txt_Resultado.Multiline = true;
            this.Txt_Resultado.Name = "Txt_Resultado";
            this.Txt_Resultado.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.Txt_Resultado.Size = new System.Drawing.Size(535, 249);
            this.Txt_Resultado.TabIndex = 2;
            // 
            // Lbl_text
            // 
            this.Lbl_text.AutoSize = true;
            this.Lbl_text.Font = new System.Drawing.Font("Garamond", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.Lbl_text.Location = new System.Drawing.Point(26, 152);
            this.Lbl_text.Name = "Lbl_text";
            this.Lbl_text.Size = new System.Drawing.Size(321, 22);
            this.Lbl_text.TabIndex = 3;
            this.Lbl_text.Text = "Nomes que contém 7 ou mais vogais:";
            // 
            // Frm_Exercicio
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(596, 450);
            this.Controls.Add(this.Lbl_text);
            this.Controls.Add(this.Txt_Resultado);
            this.Controls.Add(this.Btn_Search);
            this.Controls.Add(this.Lbl_SelecaoDeArquivo);
            this.Name = "Frm_Exercicio";
            this.Text = "Teste";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Lbl_SelecaoDeArquivo;
        private System.Windows.Forms.Button Btn_Search;
        private System.Windows.Forms.TextBox Txt_Resultado;
        private System.Windows.Forms.Label Lbl_text;
    }
}
