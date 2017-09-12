using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bugger
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool started = false;

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private async void btnStart_Click(object sender, EventArgs e)
        {
            started = true;
            var personName = txtName.Text;
            Random rand = new Random();
            
            for(int i = 3; i > 0; i = i - 1)
            {
                lblStatus.Text = i.ToString();
                await waitTime(1000);
            }

            lblStatus.Text = "Bothering";

            while (started)
            {
                SendKeys.Send(personName);
                SendKeys.Send("{ENTER}");
                await waitTime(rand.Next(300, 1100));
            }
        }

        async Task waitTime(int time)
        {
            await Task.Delay(time);
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            started = false;
            lblStatus.Text = "Not Bothering";
        }
    }
}
