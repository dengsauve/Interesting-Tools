﻿namespace Bugger
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnStart = new System.Windows.Forms.Button();
            this.btnStop = new System.Windows.Forms.Button();
            this.txtName = new System.Windows.Forms.TextBox();
            this.lblStatus = new System.Windows.Forms.Label();
            this.numericMinInterval = new System.Windows.Forms.NumericUpDown();
            this.numericMaxInterval = new System.Windows.Forms.NumericUpDown();
            this.lblMinInterval = new System.Windows.Forms.Label();
            this.lblMaxInterval = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.numericMinInterval)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericMaxInterval)).BeginInit();
            this.SuspendLayout();
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(12, 139);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(100, 23);
            this.btnStart.TabIndex = 0;
            this.btnStart.Text = "Start";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // btnStop
            // 
            this.btnStop.Location = new System.Drawing.Point(12, 168);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(100, 23);
            this.btnStop.TabIndex = 1;
            this.btnStop.Text = "Stop";
            this.btnStop.UseVisualStyleBackColor = true;
            this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(12, 12);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 20);
            this.txtName.TabIndex = 2;
            this.txtName.Text = "Name";
            // 
            // lblStatus
            // 
            this.lblStatus.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblStatus.ForeColor = System.Drawing.Color.Lime;
            this.lblStatus.Location = new System.Drawing.Point(9, 113);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(100, 23);
            this.lblStatus.TabIndex = 3;
            this.lblStatus.Text = "Not Bothering";
            this.lblStatus.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // numericMinInterval
            // 
            this.numericMinInterval.Increment = new decimal(new int[] {
            50,
            0,
            0,
            0});
            this.numericMinInterval.Location = new System.Drawing.Point(12, 51);
            this.numericMinInterval.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericMinInterval.Minimum = new decimal(new int[] {
            250,
            0,
            0,
            0});
            this.numericMinInterval.Name = "numericMinInterval";
            this.numericMinInterval.ReadOnly = true;
            this.numericMinInterval.Size = new System.Drawing.Size(100, 20);
            this.numericMinInterval.TabIndex = 4;
            this.numericMinInterval.Value = new decimal(new int[] {
            250,
            0,
            0,
            0});
            // 
            // numericMaxInterval
            // 
            this.numericMaxInterval.Increment = new decimal(new int[] {
            50,
            0,
            0,
            0});
            this.numericMaxInterval.Location = new System.Drawing.Point(12, 90);
            this.numericMaxInterval.Maximum = new decimal(new int[] {
            3000,
            0,
            0,
            0});
            this.numericMaxInterval.Minimum = new decimal(new int[] {
            1100,
            0,
            0,
            0});
            this.numericMaxInterval.Name = "numericMaxInterval";
            this.numericMaxInterval.ReadOnly = true;
            this.numericMaxInterval.Size = new System.Drawing.Size(100, 20);
            this.numericMaxInterval.TabIndex = 5;
            this.numericMaxInterval.Value = new decimal(new int[] {
            1100,
            0,
            0,
            0});
            // 
            // lblMinInterval
            // 
            this.lblMinInterval.AutoSize = true;
            this.lblMinInterval.ForeColor = System.Drawing.Color.Lime;
            this.lblMinInterval.Location = new System.Drawing.Point(12, 35);
            this.lblMinInterval.Name = "lblMinInterval";
            this.lblMinInterval.Size = new System.Drawing.Size(86, 13);
            this.lblMinInterval.TabIndex = 6;
            this.lblMinInterval.Text = "Minimum Interval";
            // 
            // lblMaxInterval
            // 
            this.lblMaxInterval.AutoSize = true;
            this.lblMaxInterval.ForeColor = System.Drawing.Color.Lime;
            this.lblMaxInterval.Location = new System.Drawing.Point(12, 74);
            this.lblMaxInterval.Name = "lblMaxInterval";
            this.lblMaxInterval.Size = new System.Drawing.Size(89, 13);
            this.lblMaxInterval.TabIndex = 7;
            this.lblMaxInterval.Text = "Maximum Interval";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.ClientSize = new System.Drawing.Size(125, 202);
            this.Controls.Add(this.lblMaxInterval);
            this.Controls.Add(this.lblMinInterval);
            this.Controls.Add(this.numericMaxInterval);
            this.Controls.Add(this.numericMinInterval);
            this.Controls.Add(this.lblStatus);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.btnStop);
            this.Controls.Add(this.btnStart);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "Form1";
            this.Opacity = 0.85D;
            this.ShowIcon = false;
            this.Text = "BotherTron";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numericMinInterval)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericMaxInterval)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Button btnStop;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label lblStatus;
        private System.Windows.Forms.NumericUpDown numericMinInterval;
        private System.Windows.Forms.NumericUpDown numericMaxInterval;
        private System.Windows.Forms.Label lblMinInterval;
        private System.Windows.Forms.Label lblMaxInterval;
    }
}

