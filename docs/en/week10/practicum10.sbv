0:00:00.500,0:00:07.230
[Student] Have you been to Isoldi in New York? I love their lasagna. [Alfredo] No, I haven't been to

0:00:07.230,0:00:15.470
Isoldi. I usually go to two places, one is called , it's here on 33rd and 3rd

0:00:15.470,0:00:20.279
Avenue, it's just Sicilian, very authentic I love

0:00:20.279,0:00:23.220
it. The other one which is absolutely the

0:00:23.220,0:00:28.170
best pizza in the world, it's called Sorbillo, it's very

0:00:28.170,0:00:34.410
close to NYU. The pizza is just like in Naples and it's like you can't find

0:00:34.410,0:00:39.329
anything better on this planet, so you know, you should go to Sorbillo. And if

0:00:39.329,0:00:45.500
you mention my name you get discount, right, so yeah I have a special power.

0:00:45.500,0:00:51.989
Yeah... Chicago pizza is not pizza, it's pie. So if you call it

0:00:51.989,0:00:58.820
Chicago pie, it's fantastic, it's not pizza. Napoli pizza is the only pizza.

0:00:58.820,0:01:04.920
Okay, all right, so what do we talk today about? Today we talk about something

0:01:04.920,0:01:10.830
called The Truck Backer-Upper. What are we trying to do today in this lecture? So

0:01:10.830,0:01:14.340
this is the first lecture where you're going to help me, basically reading with you

0:01:14.340,0:01:20.280
along, a paper such that we can figure out whether things make sense.

0:01:20.280,0:01:25.530
This is how we educate ourselves in the research world, you don't have

0:01:25.530,0:01:31.079
necessarily Yann on your side all the time so you have to read papers and you

0:01:31.079,0:01:35.490
have to make sense of what's written there. Usually I transcribe them

0:01:35.490,0:01:41.729
back with Typora just to fix the main topics in in my mind, and

0:01:41.729,0:01:45.540
to commit to time such that I can check

0:01:45.540,0:01:51.509
later what's going on. So let's get started. So what is this setup?

0:01:51.509,0:01:56.969
what are we trying to do here? So we are trying to design by self-learning of a

0:01:56.969,0:02:01.590
nonlinear controller to control the steering of a trailer truck while

0:02:01.590,0:02:07.170
backing up to a loading dock from an arbitrary initial position. Only backing

0:02:07.170,0:02:11.819
up is allowed. So what does this mean? What we are trying to do is going to be

0:02:11.819,0:02:17.760
learning how to drive a truck, which is maybe not that complicated if

0:02:17.760,0:02:25.020
you go forward, but we are trying to park a truck, so it just goes backwards and only

0:02:25.020,0:02:31.110
backwards. So you know if you try to park your car in a parallel parking, it's a

0:02:31.110,0:02:37.080
little bit complicated perhaps sometimes and not always you can get it done with

0:02:37.080,0:02:44.180
one manoeuvre, if you have a trailer truck attached to your back it's a mess.

0:02:44.180,0:02:51.870
We are figuring out this very soon. So how does this trailer truck

0:02:51.870,0:02:58.830
works? We have two items, we have a cab which is the top right part there, so we

0:02:58.830,0:03:04.110
have an angle of the cab with respect to the x-axis, and then we have

0:03:04.110,0:03:09.209
the coordinates x and y of the  joint between the cab and the trailer.

0:03:09.209,0:03:16.470
Okay then in the part below we have the trailer and therefore we have like the

0:03:16.470,0:03:21.540
x and y location of the back of the trailer truck and then we have the theta trailer,

0:03:21.540,0:03:25.500
which is telling us what is the angle of this trailer truck with respect to the

0:03:25.500,0:03:33.150
x-axis. Our objective is to drive this guy backwards until the back of the

0:03:33.150,0:03:38.970
trailer hits basically the dock location, which is represented there with the x_dock

0:03:38.970,0:03:46.380
and y_dock coordinate. Moreover, we would like to have the theta trailer

0:03:46.380,0:03:52.440
which is the angle of the trailer to be 0 such that the trailer is

0:03:52.440,0:03:58.739
orthogonal to the docking station and basically the rear part of the... the rear

0:03:58.739,0:04:02.310
part, front and rear,  is 'rear' back, right?

0:04:02.310,0:04:06.269
I'm speaking English, I guess it's correct. So the rear part of the

0:04:06.269,0:04:13.019
trailer should be parallel to the docking station and as close as

0:04:13.019,0:04:21.690
possible to the location of the dock. So far make sense, right? Yeah, ok, all right.

0:04:21.690,0:04:27.570
So let's read a little bit more further in this paper, so we have some

0:04:27.570,0:04:36.240
state variables, there are six, which I think this is perhaps not

0:04:36.240,0:04:41.580
correct, we'll figure this out soon. So the state variables are the theta_cab

0:04:41.580,0:04:47.760
which is the angle of the truck. Then  x_cab and y_cab, which is the Cartesian

0:04:47.760,0:04:54.360
position of the yoke, which is the part behind the cab. And then you have x_trailer and

0:04:54.360,0:05:00.000
y_trailer which is the position of the rear of the trailer, plus theta trailer

0:05:00.000,0:05:05.640
which is the angle of the trailer. Okay. So basically, how the 

0:05:05.640,0:05:08.400
procedure goes is the following: The

0:05:08.400,0:05:12.980
truck backs up until it hits the dock and then it stops.

0:05:12.980,0:05:18.120
The goal is to back the trailer to be parallel to the loading

0:05:18.120,0:05:21.930
dock, right? So the the goal is to have the back side of the trailer to

0:05:21.930,0:05:27.150
be parallel to the docking station. And then, having the x_trailer and y_trailer, 

0:05:27.150,0:05:33.450
the location of the back of the trailer, as close as possible to the x_dock

0:05:33.450,0:05:37.770
and y_dock. Okay, are you with me so far?

0:05:37.770,0:05:42.450
So the initial position is going to be randomly set and then we had to back up

0:05:42.450,0:05:49.830
until we hit the trailer and the dock

0:05:49.830,0:05:57.240
with the back of the trailer and we are exactly orthogonal. Okay? There are a

0:05:57.240,0:06:04.410
few difficulties with this, and we're gonna figure out right now what

0:06:04.410,0:06:15.540
these difficulties are. All right, so we go  cd Work/GitHub/pDL. Then now we go conda activate pDL

0:06:15.540,0:06:23.010
right? Now here we have a Jupiter notebook. So in this case we are going to

0:06:23.010,0:06:30.090
go over this truck_backer-upper. Something I really like to do in

0:06:30.090,0:06:35.640
Jupiter notebook is to use actually unicode, since we are using

0:06:35.640,0:06:39.419
Python 3 we can use unicode, right? So to write pi there

0:06:39.419,0:06:44.970
I just need to \pi  and tab and you get π. Or you

0:06:44.970,0:06:55.290
can do \alpha \beta \gamma, okay? This is not coding, this is notebooks so you can

0:06:55.290,0:07:01.980
do ugly things like this. Alright so I just initialize some libraries, this is

0:07:01.980,0:07:09.500
our setup, I initialize some object here we don't care right now and we start by

0:07:09.500,0:07:14.670
visualizing this guy here, okay? And I think I had one zoom a little bit

0:07:14.670,0:07:25.350
because you can't see. There you go, cool. Okay so now we start the interactive part. We'd like

0:07:25.350,0:07:32.160
to draw this guy, so let's say with zero angle of the steering wheel

0:07:32.160,0:07:38.820
and I keep executing this, alright? So this guy here keeps

0:07:38.820,0:07:48.360
going and then what's happening here after the next step is that my computer

0:07:48.360,0:07:53.910
now is complaining and there you go, so you get the truck is

0:07:53.910,0:07:59.160
jackknifed. What does it mean the truck has is jackknifed? It means you simply broke your

0:07:59.160,0:08:03.750
truck because you drove into yourself. That's very interesting but you can

0:08:03.750,0:08:11.850
drive inside yourself with these trucks. So let me reset the state with

0:08:11.850,0:08:17.820
something a bit decent, maybe like... okay someone, any volunteers? what is

0:08:17.820,0:08:24.150
going to be now the angle you'd like me to steer the wheel? You can give me

0:08:24.150,0:08:29.910
anything from 0 to 45 degrees, I think. -10, okay so I go -10 which is gonna

0:08:29.910,0:08:39.140
be turning to the right 10 degrees and I go 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 steps. 

0:08:39.140,0:08:44.400
If I keep going you're gonna be jackknifing soon. Okay? So what should I

0:08:44.400,0:08:53.310
do right now? someone else? or maybe still you. +15. Okay, let's try +15 degrees.

0:08:53.310,0:09:00.880
We go 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Hmm okay. What next? Should I

0:09:00.880,0:09:05.260
keep going? Yeah,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10. We are gonna be

0:09:05.260,0:09:12.160
going off screen. Maybe alternate plus and minus? Then you go straight, right? If

0:09:12.160,0:09:16.450
I keep going like this you can see that this truck is gonna be going outside,

0:09:16.450,0:09:22.750
we're gonna be, you know, going basically game over, so you don't have a driving

0:09:22.750,0:09:28.420
license. So -15, okay? Do you agree all? should I go with

0:09:28.420,0:09:37.660
-15? I go with -15. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 Ok now we cannot drove drive forward.

0:09:37.660,0:09:43.860
+45. We messed up. No no I don't think you messed up I think it's still good.

0:09:43.860,0:09:50.050
0. okay someone said 0 let's try with 0. Not yet, okay, what do you want

0:09:50.050,0:10:04.450
me to do? +45. Okay, +45. I can keep going but then we are gonna be just... oh oh,

0:10:04.450,0:10:17.050
yeah. One more -45 okay, let's go -45 twice, then twice more, then I'm

0:10:17.050,0:10:22.540
gonna go oh wait no, six more, so 1, 2, 3, 4 ,5 , 6. OK.

0:10:22.540,0:10:27.250
So if I keep going like this we are gonna be going off the screen, right? So I

0:10:27.250,0:10:31.870
think you got the picture, right? Is it twice more? No, it's an older

0:10:31.870,0:10:37.030
message. Okay, the point here is that this stuff it's a bit you know tricky.

0:10:37.030,0:10:42.280
You can get the hang of it and maybe the

0:10:42.280,0:10:45.700
final solution is going to be like something where we go like

0:10:45.700,0:10:51.940
this and then we go in the other direction to rotate, something like +10

0:10:51.940,0:11:01.360
and then it's gonna be killing each other here, so plus maybe 25 or maybe,

0:11:01.360,0:11:03.930
let's see... Maybe +20, see? so we can turn around and

0:11:11.420,0:11:21.529
now we should basically undo this thing. So if I go like, I think +40, and

0:11:21.529,0:11:30.079
there you go. And we can go basically straight. Still

0:11:30.079,0:11:39.350
something, +20 maybe? Okay? and then we can go zero... See? I've been teaching this

0:11:39.350,0:11:45.769
forever so you know I can actually drive this thing, okay? So there you go, 

0:11:45.769,0:11:51.110
Alf is a truck driver. There you go, see?  oh my God, I'm actually managing to do this. We

0:11:51.110,0:11:57.050
had to fix a little bit, honk honk yeah, honk the horn, I actually had my horn

0:11:57.050,0:12:05.110
there, so we had to actually oo-oh  oh no no okay sorry.

0:12:07.170,0:12:13.149
Okay fine. So this is actually considered success. Okay now my computer now is

0:12:13.149,0:12:17.439
complaining because there is some lag. I should have a turned a little bit before.

0:12:17.439,0:12:21.999
Anyhow, the point  is that it's

0:12:21.999,0:12:26.170
not quite straightforward to figure

0:12:26.170,0:12:30.759
out how to drive this guy, because it's highly nonlinear, so we had to figure

0:12:30.759,0:12:36.540
out how to implement a high nonlinear system, how to invert a high nonlinear

0:12:36.540,0:12:41.470
kinematic model basically, such that if we had a kinematic model, you know how

0:12:41.470,0:12:45.730
the vehicle behaves given an action, if you invert the kinematic model

0:12:45.730,0:12:50.019
you figure out what action you would like to take in order to drive

0:12:50.019,0:12:54.999
to a final destination. But since we don't know how to do this analytically,

0:12:54.999,0:12:59.470
or maybe we didn't know in the 90's, we can train a neural net and then

0:12:59.470,0:13:05.709
we can simply figure out whether we can learn how to

0:13:05.709,0:13:11.079
to drive backwards. Okay, are you excited? are

0:13:11.079,0:13:15.819
you interesting to know how we can do this? Yeah? No?

0:13:15.819,0:13:27.209
Yes! okay let me think. So the overall 

0:13:27.209,0:13:36.009
objective here is gonna be that given an initial position in this map here, 

0:13:36.009,0:13:40.600
I'd like to know what sequence of actions, which is gonna

0:13:40.600,0:13:47.620
be basically what sequence of steering angle for the wheels, I should apply in

0:13:47.620,0:13:52.899
this six dimensional space, so it's not just 2D. This

0:13:52.899,0:13:57.370
screen here is gonna be the 2D screen but then you have six values, right? You

0:13:57.370,0:14:02.019
have the (x, y) of the cabs, (x, y) of the trailer and the two angles, so you have a six

0:14:02.019,0:14:06.699
dimensional space and then in this six dimensional space you'd like to infer,

0:14:06.699,0:14:10.839
so you get a network which is telling you: For this

0:14:10.839,0:14:14.050
specific configuration of the truck or the trailer truck you should be

0:14:14.050,0:14:18.899
outputting this specific value, it is a regression network somehow.

0:14:18.899,0:14:24.029
It's going to be outputting a scalar which is going from -45 to

0:14:24.029,0:14:32.759
+45 I think. Yeah, yeah, I think so, I think that's the range. For every

0:14:32.759,0:14:37.139
position. So our goal is gonna be training a neural net that goes from

0:14:37.139,0:14:42.209
points in this six dimensional space to one scalar, which is gonna be the scalar

0:14:42.209,0:14:48.749
that allows me to get  a sequence of scalars, so one

0:14:48.749,0:14:54.809
scalar at the time, such that you would like to drive these track backwards to

0:14:54.809,0:14:59.369
the final destination. Did I make sense? Does it make sense?

0:14:59.369,0:15:06.029
Maybe I was confused. Is it okay?  Alright, so let's figure out how to get

0:15:06.029,0:15:12.990
all this stuff going. Back to the slides. Training. So the

0:15:12.990,0:15:18.420
training involves two stages: The first one we have to train a network, 

0:15:18.420,0:15:24.449
a neural net, to be an emulator of the truck and trailer kinematics. This is how

0:15:24.449,0:15:28.379
the paper have done,  so that's not the only option but it's

0:15:28.379,0:15:33.569
what we are going for; Then a second stage involves training of a neural

0:15:33.569,0:15:36.870
network controller, to control the emulator, which is gonna be basically

0:15:36.870,0:15:40.920
doing the task that we were doing right now when we were coming up with

0:15:40.920,0:15:47.040
a value for this steering angle such that we can reach destination. And 

0:15:47.040,0:15:50.839
destination, like success is determined by two factors:

0:15:50.839,0:15:59.100
closeness to the docking station and the orientation of the trailer. So this is the

0:15:59.100,0:16:03.689
overall diagram. You are going to have a  neural net, a controller, which was me right now

0:16:03.689,0:16:07.920
following your suggestions through the chat which is providing you this

0:16:07.920,0:16:14.009
steering signal at the discrete time interval k. Then we have a

0:16:14.009,0:16:18.329
trailer-truck kinematics which are the equations that allowed me to 

0:16:18.329,0:16:24.389
tell you what is the next configuration of the truck which is 

0:16:24.389,0:16:28.860
giving you the next state, given that you provide the previous state inside and

0:16:28.860,0:16:32.900
then the steering signal. And this Delta here is simply

0:16:32.900,0:16:37.700
time delay that tells you that this is the next state. 

0:16:37.700,0:16:43.330
These are  diagrams from the

0:16:43.330,0:16:47.900
electronics, like Electrical Engineering diagrams, because

0:16:47.900,0:16:54.140
there was no computer science back in the day. Alright,

0:16:54.140,0:17:01.520
so a state k is fed to the controller which provides a steering signal k

0:17:01.520,0:17:08.240
between -1 in this case and +1 for the truck. So they kind of use a Tanh

0:17:08.240,0:17:15.110
at the output. At the time index is k. Each time cycle, the truck backs up by a fixed

0:17:15.110,0:17:21.200
small distance. So these are the equations for the trailer-truck with

0:17:21.200,0:17:27.860
several trucks. You had the location of the x and y of the cab, and then, 

0:17:27.860,0:17:32.900
given that you know the distance, the length both of the the cab and also

0:17:32.900,0:17:39.100
of the trailers, you can estimate what is the

0:17:39.100,0:17:47.450
variation of the angle given the input phi. The phi is this negative angle

0:17:47.450,0:17:53.150
because it's on the right-hand side. So we have that s is the signed speed

0:17:53.150,0:17:57.350
so you can go forward and backward and then phi is this negative steering angle,

0:17:57.350,0:18:01.450
positive angles being on the right-hand side so it's like

0:18:01.450,0:18:08.680
swapped. And then x and y is the location here at the back of the of the cab.

0:18:08.680,0:18:15.710
Notice now that basically you have the x and y position of the trailer is

0:18:15.710,0:18:21.860
actually determined by the x and y position of the cab and the distance d1

0:18:21.860,0:18:27.950
and the theta_1. Okay so before I was telling you that we had

0:18:27.950,0:18:33.710
six values for the state, but as you can tell from now, we just need four values.

0:18:33.710,0:18:38.930
You have the x and y, and you have the theta_0 which is the

0:18:38.930,0:18:43.280
angle of the cab and then theta_1 that is the angle of the trailer,

0:18:43.280,0:18:49.400
so you have only four independent values. Here these x and y

0:18:49.400,0:18:55.180
of the trailer is completely determined given these other values.

0:18:55.180,0:19:04.070
Question: Aren't these velocities? So these are the equations, yes so this is

0:19:04.070,0:19:08.210
how the the position changes, so these are velocities, but whenever you

0:19:08.210,0:19:14.690
have a state, the state in this case is x, y, theta_0, theta_1, and then whenever

0:19:14.690,0:19:17.270
you'd like to write the equation of the motion,

0:19:17.270,0:19:22.100
you're gonna write the variation in time, sothe

0:19:22.100,0:19:28.010
velocity of x, velocity over y, the angular velocity over this guy, and the

0:19:28.010,0:19:32.690
angular velocity of the other guy are gonna be expressed by these equations in

0:19:32.690,0:19:36.650
continuous-time. Then we're going to be discretizing them since we are using a

0:19:36.650,0:19:42.380
computer. But this is how we will express a dynamic model,

0:19:42.380,0:19:48.770
a model that evolves in time. All right so we have the equations. Let's

0:19:48.770,0:19:53.300
figure out now how we train these networks. So this is how we train the

0:19:53.300,0:19:58.370
network for emulating the truck, trailer-truck kinematics. On the left

0:19:58.370,0:20:02.540
hand side we provide a random input which is going to be is going to be like

0:20:02.540,0:20:09.650
a random initial value for the steering angle and then we provide this

0:20:09.650,0:20:14.990
random steering angle to the truck dynamics which is going to tell me: Given

0:20:14.990,0:20:20.090
the previous state, what is what is going to be the next state? And then on the

0:20:20.090,0:20:24.110
bottom part I'm gonna have my first network which is gonna be trained as a

0:20:24.110,0:20:28.040
regressor and it's going to be trying to minimize the difference

0:20:28.040,0:20:34.130
between the actual next state and this state that is predicted. Then

0:20:34.130,0:20:40.100
the difference between the prediction and the actual ground truth is used in

0:20:40.100,0:20:46.730
order to, and the term they are using the article is adapt

0:20:46.730,0:20:53.450
the weights of this network, which is basically train the network, so

0:20:53.450,0:20:58.340
how you how do you update the weights of the network? The weights of the network

0:20:58.340,0:21:02.330
are updated by using this error, so question now is

0:21:02.330,0:21:06.590
going to be for you: What kind of loss function are they

0:21:06.590,0:21:12.950
using here? Since the signal that is used to update these weights is actually

0:21:12.950,0:21:18.830
the difference between the target and the actual prediction.

0:21:18.830,0:21:24.049
You should be able to tell me now, it's actually in the midterm right now, it's

0:21:24.049,0:21:26.769
one of the question. MSE. Why MSE? Because if you compute the

0:21:30.090,0:21:34.979
derivative of the MSE you get the difference 

0:21:34.979,0:21:40.799
between your prediction and the 

0:21:40.799,0:21:47.359
target.So this difference, which is here swapped, right?

0:21:47.359,0:21:53.909
is actually used here to change the values. In our course we perform

0:21:53.909,0:21:58.049
gradient descent, so you get the positive Delta, you have

0:21:58.049,0:22:02.340
prediction minus ground truth and then you use that one to compute the partial

0:22:02.340,0:22:07.619
derivatives, and then you subtract that to the parameter, such that you go in

0:22:07.619,0:22:11.309
the opposite direction. Here they actually use the inverted sign,

0:22:11.309,0:22:16.619
this prediction minus the ground truth is factor for adapting,

0:22:16.619,0:22:20.999
which is changing, these parameters, but basically is the

0:22:20.999,0:22:28.169
same thing. There is a question: Why are we training the emulator if you already

0:22:28.169,0:22:32.419
have a model for the track movement? Okay that's a very good question.

0:22:32.419,0:22:37.590
Because in this case we have equations and therefore we could actually get a

0:22:37.590,0:22:42.840
partial derivatives through these questions but you may not have the

0:22:42.840,0:22:47.970
equations, let's say you have a much more complex system, you may just

0:22:47.970,0:22:55.799
observe several experts driving this you know complex systems and then

0:22:55.799,0:23:00.929
you actually, through this sequence of trajectories,

0:23:00.929,0:23:06.570
sequence of states variables, you can learn a network

0:23:06.570,0:23:12.299
that is able to emulate what is the kinematics of

0:23:12.299,0:23:18.899
this system, okay? That was the answer for Joseph. Alright,

0:23:18.899,0:23:24.269
cool. So right now let's see how this keeps going, or maybe 

0:23:24.269,0:23:30.960
let me actually switch to this guy here. Right so let's actually

0:23:30.960,0:23:36.989
start training this stuff. So we get Torch, and then we're

0:23:36.989,0:23:39.950
gonna be running this for loop at the beginning.

0:23:39.950,0:23:44.540
And so what happens here is gonna be, you know, we provide some random initial

0:23:44.540,0:23:50.270
steering angle and then we use the kinematics model to learn what is

0:23:50.270,0:23:54.500
the connection between previous state and next state. Whenever the track goes

0:23:54.500,0:24:00.560
outside we just kill it, and these keeps going until we we

0:24:00.560,0:24:05.960
have enough points such that we can train these network to emulate the

0:24:05.960,0:24:10.040
trailer-truck kinematics. Again, in this case it wouldn't be necessary

0:24:10.040,0:24:13.670
because we have the equations, but let's say we don't have the equations

0:24:13.670,0:24:18.260
but we just have observations from the real world, then you

0:24:18.260,0:24:22.610
actually have to  learn those functions such that

0:24:22.610,0:24:29.180
we can differentiate from, we can run gradients through. So if we keep going

0:24:29.180,0:24:34.400
like that my computer is gonna crash. So right now you can see that this is

0:24:34.400,0:24:38.750
taking forever. Why is taking forever? Because there is this visualization, so

0:24:38.750,0:24:44.480
in this case I turn off the visualization such that it doesn't draw

0:24:44.480,0:24:49.790
things there and then I can run now for 10,000 times. Oh okay, and

0:24:49.790,0:24:54.410
this happened because I interrupted the script, okay how

0:24:54.410,0:24:59.840
lovely. Okay boom. This is quite quick 

0:24:59.840,0:25:05.540
because it doesn't have the rendering. [Student] So with the emulator

0:25:05.540,0:25:14.690
you are emulating what players playing the game would do? [Alfredo] So the emulator here is

0:25:14.690,0:25:19.690
gonna be trying to learn what is the next state given the previous state

0:25:19.690,0:25:25.370
given I provide a specific random steering signal here. So given a

0:25:25.370,0:25:30.680
state and given a steering angle I try to learn what is the next state, and this

0:25:30.680,0:25:36.230
is coming from the ground truth which is this box here. This is not a

0:25:36.230,0:25:40.160
recurrent net, it's just a normal net, you have an input which is

0:25:40.160,0:25:45.080
state plus action and then the output is going to be just action, there is no

0:25:45.080,0:25:51.850
recurrence right now. The signals are always random at every step,

0:25:51.850,0:25:57.340
the steering signal is random. The state,I collect the whole trajectory

0:25:57.340,0:26:04.420
while I input a random steering angle. Okay, very long question: Does this

0:26:04.420,0:26:10.150
matter that the data you're collecting

0:26:10.150,0:26:14.920
is a bit different from the human test time action? The data you're

0:26:14.920,0:26:21.250
collecting changes directions rapidly frequently.

0:26:21.250,0:26:26.380
There is no time. Here my training, we haven't talked about training yet...

0:26:26.380,0:26:33.550
So this is gonna be a just normal neural net that given a input

0:26:33.550,0:26:41.080
state is gonna map it to the output state given a specific angle for

0:26:41.080,0:26:47.680
the wheels, there is no time. So you have one state you have one angle that's

0:26:47.680,0:26:56.550
the output, no time right now.  Okay so we go here, these are my inputs

0:26:56.550,0:27:01.600
and the outputs, like that I collected over these trajectories so if you check

0:27:01.600,0:27:08.410
here I just have the initial initial state, I get the state from the

0:27:08.410,0:27:13.690
truck, then I have a phi which is my angle which is going to be

0:27:13.690,0:27:19.930
something between random minus 0.5, so from -45 to +45.

0:27:19.930,0:27:24.820
Then I have my input, so it's gonna be the state plus the angle and

0:27:24.820,0:27:27.850
then the output is going to be the output of the truck

0:27:27.850,0:27:34.630
which has step with angle phi.  Alright, so we have this thing here, I can

0:27:34.630,0:27:43.140
can create my network and then I can start

0:27:43.250,0:27:49.460
training my network. And this will keep going until forever, but then basically

0:27:49.460,0:27:54.980
here we are trying to get a neural net which is simply a couple of layers, here

0:27:54.980,0:28:00.320
right so Linear, ReLU, Linear. We start from steering 

0:28:00.320,0:28:06.110
size which is 1 plus the state size which was

0:28:06.110,0:28:14.030
6, like the x and y and angle for both 

0:28:14.030,0:28:20.000
the cab and the trailer. Then you have a number of hidden units which are

0:28:20.000,0:28:23.870
gonna be described now in the paper, then have a ReLU, and then a

0:28:23.870,0:28:27.250
final Linear output. MSE and SGD. Alright, let's go

0:28:32.900,0:28:42.220
back to the presentation. So Figure 3, which is the this one, shows 

0:28:42.220,0:28:49.160
how to train the emulator. So the truck backs up randomly and the

0:28:49.160,0:28:53.540
emulator learns to generate the next position state vector given the present

0:28:53.540,0:28:58.850
state vector and the steering signal. And you can hear now my computer fan

0:28:58.850,0:29:05.540
spinning because it's training ok. Sorry for the bad audio. Alright, so this is how

0:29:05.540,0:29:09.730
we train this system, how do you train the controller. So this is state

0:29:09.730,0:29:15.350
transition flow diagram. C represents the controller, so it's another neural net

0:29:15.350,0:29:20.960
whereas T represents the truck and trailer emulator, So all the truck

0:29:20.960,0:29:29.240
kinematics or the trailer emulator, either or. So how is this thing working?

0:29:29.240,0:29:35.450
How is now time added to the system? So we start with this controller C,

0:29:35.450,0:29:43.100
this controller C, we said, provides what? The steering angle to the truck or

0:29:43.100,0:29:50.690
the truck emulator. So the controller provides an angle given that is fed with

0:29:50.690,0:29:57.140
the initial state, which we can call h of K minus 1 timestamp.

0:29:57.140,0:30:03.800
And if we provide these previous states to the controller

0:30:03.800,0:30:09.980
and the truck, the truck we basically get the next state. So you can think about

0:30:09.980,0:30:19.030
these two guys as just one element of a recurrent network which has

0:30:19.030,0:30:24.050
no input, or well it could have an input but the input is not connected

0:30:24.050,0:30:28.610
so this is like one of the multiple cells we usually seen in a

0:30:28.610,0:30:34.300
recurrent net, but there is a different diagram inside. So how do we train this

0:30:34.300,0:30:40.070
item? Well, you already know the answer, right? So you get this one

0:30:40.070,0:30:44.390
down here, we don't have any input on the bottom, and then you stack

0:30:44.390,0:30:47.900
another one, you stack on another one, and then you keep going until you actually

0:30:47.900,0:30:52.910
start from the initial location of the truck which is the initial hidden state

0:30:52.910,0:30:58.300
or which is basically the initial truck location and configuration. 

0:30:58.300,0:31:02.780
And then, on the right hand side you keep going

0:31:02.780,0:31:09.020
and then whatever until the end, where you reach the final point, which

0:31:09.020,0:31:14.360
final condition can be a few of the following: Run out of steps, jackknife or

0:31:14.360,0:31:19.070
third part: You hit one of the edges and then I check what is the distance

0:31:19.070,0:31:24.560
between your back and the docking station and then I check what is your

0:31:24.560,0:31:30.830
angle or your orientation of the truck which should have been horizontal.

0:31:30.830,0:31:36.860
So those are the answers to the question: What are the terminal

0:31:36.860,0:31:42.470
conditions. There are three terminal conditions: Jackknifing, running out of

0:31:42.470,0:31:49.550
steps, or hitting an edge and whenever you hit an edge you want to

0:31:49.550,0:31:54.200
actually minimize now what is the distance between the

0:31:54.200,0:31:59.990
docking station and then you want to try to minimize whatever angle you get 

0:31:59.990,0:32:06.629
for the trailer. Cool. So figure five: Training the

0:32:06.629,0:32:12.389
controller with backpropagation. As you you saw before in the previous

0:32:12.389,0:32:16.710
diagram we were  training the emulator, we have

0:32:16.710,0:32:23.009
something similar with this feedback loop. The final state, so after

0:32:23.009,0:32:28.230
you complete this whole trajectory, the final state will be ending with some

0:32:28.230,0:32:33.480
specific configuration. I enforce this final state to be as close as possible

0:32:33.480,0:32:39.389
to my target state which means you want to have the x_trailer as close

0:32:39.389,0:32:43.200
as possible to the dock trailer, the  y_trailer as close as possible to

0:32:43.200,0:32:49.200
y_dock and then the final angle of the trailer, you know horizontals so equal to 0.

0:32:49.200,0:32:55.620
Then you make the difference and you send the difference back to adapt

0:32:55.620,0:33:00.299
these weights, but of course it's not just a line, the whole thing goes through

0:33:00.299,0:33:05.190
as usual chain rule. So this actually travels through

0:33:05.190,0:33:10.409
all previous T/C, so it goes inside modules. The visualization shows that

0:33:10.409,0:33:16.139
only the 'C', the controller blocks, are updated, also proportionally to the final

0:33:16.139,0:33:20.610
error, which implies an MSE loss. Again, the other thing that we came up with

0:33:20.610,0:33:27.210
before. Cool. So the initial position is set at random,

0:33:27.210,0:33:34.220
the track backs up until it stops. Final error is just for back-propagation and

0:33:34.220,0:33:40.519
this is back-propagation through time with a variable unrolling period k. 

0:33:40.519,0:33:46.110
So the weight changes in C, the controller, are taken as the sum of the

0:33:46.110,0:33:53.190
tentative changes. What is the meaning of this sentence? Well now you

0:33:53.190,0:34:02.790
maybe appreciate why PyTorch is accumulating the gradients every time.

0:34:02.790,0:34:08.790
Do see the point? So in this case you get this gradient coming back from the

0:34:08.790,0:34:14.540
future back to the past, and then the meaningful thing is gonna be

0:34:14.540,0:34:19.500
accumulating all these gradients, right? Because we have reused the same module

0:34:19.500,0:34:25.230
multiple times, when you go and perform back-propagation this back-propagation

0:34:25.230,0:34:33.270
will sum up things, as many times as we went through this module.

0:34:33.270,0:34:36.570
Right? That's why PyTorch accumulates gradient

0:34:36.570,0:34:41.460
whenever you compute backdrop. If it would be just computing them

0:34:41.460,0:34:45.110
and replacing whatever it was before, then you just have the gradients of the

0:34:45.110,0:34:51.350
oldest iteration, the one most back in the past.

0:34:51.350,0:34:57.570
Instead in this case, which what which is written here, which say is that the all

0:34:57.570,0:35:02.550
the tentative changes are summed together means you accumulate

0:35:02.550,0:35:09.840
the gradient over time. Okay, cool. Finally repeat another initial position

0:35:09.840,0:35:15.720
back up until he stops. So the network detail, this is

0:35:15.720,0:35:21.870
architecture diagrams of network architectures back in in the 90's you

0:35:21.870,0:35:27.150
start with six values for the state x and y and theta, x and Y and theta for

0:35:27.150,0:35:34.050
the two items, then you get through these items here that are called

0:35:34.050,0:35:40.020
potentiometers which are basically variable resistance which are

0:35:40.020,0:35:44.460
representing these variable weights. Variable weights as in weights

0:35:44.460,0:35:48.810
that can be tuned, okay? So these are tunable weights, so weights in a neural net.

0:35:48.810,0:35:52.350
Okay but again this is the symbol for a tunable resistor.

0:35:52.350,0:35:59.280
You have 25 of these guys, so from 6 we go to 25 and then from 25

0:35:59.280,0:36:04.430
we go to 1 which is a steering signal. So first affine transformation squashing,

0:36:04.430,0:36:09.300
second affine transformation squashing and then this guy is gonna be the

0:36:09.300,0:36:16.790
emulator, so you go from 7 which is 6 of the state plus the steering angle

0:36:16.790,0:36:23.310
to 45. So you have a fine transformation squashing, and then from these final 45

0:36:23.310,0:36:28.980
you have an affine transformation to 6 which is the final next state.

0:36:28.980,0:36:36.150
Cool. So that's it, right? So analogous to a

0:36:36.150,0:36:42.240
neural net having a number of affine transformations equal to 4 times the

0:36:42.240,0:36:48.990
number of backing up steps. So for every trajectory we train a net

0:36:48.990,0:36:55.620
which has a length that is depending on how many time steps this

0:36:55.620,0:37:04.800
specific truck took in order to reach one stopping 

0:37:04.800,0:37:11.790
condition... yeah, stopping condition.

0:37:11.790,0:37:16.620
Alright so the number of steps varies with the initial position of the

0:37:16.620,0:37:19.410
trailer  or the truck and the trailer.

0:37:19.410,0:37:26.040
So you train the core item of this network, which has several

0:37:26.040,0:37:33.300
steps or several layers, the length of these network changes based on each

0:37:33.300,0:37:39.480
specific episode and then we train this stuff with back-propagation and each

0:37:39.480,0:37:42.360
module is the same module replicated multiple times

0:37:42.360,0:37:47.520
therefore the gradients have to be summed as you go through, as that's what

0:37:47.520,0:37:55.260
PyTorch does. Makes sense? Cool. So these are a few examples: You

0:37:55.260,0:38:00.420
start with this initial position and then after a few steps the network

0:38:00.420,0:38:06.210
manages to reach the destination. Another one is here, they started with the

0:38:06.210,0:38:12.450
trailer pointing away from the dock and you can see here how it manages to

0:38:12.450,0:38:16.980
circulate around and to get you know back to the correct location. And the

0:38:16.980,0:38:21.390
final state is horizontal, so it looks almost

0:38:21.390,0:38:26.340
horizontal. Or this ono, you start orthogonal in a jackknife position right,

0:38:26.340,0:38:30.180
that's really like being bastards but nevertheless the network

0:38:30.180,0:38:39.530
can figure out how to solve this very difficult configuration. And then,

0:38:39.530,0:38:43.560
this is also really annoying but you know the network doesn't

0:38:43.560,0:38:49.460
complain. Be like on your network... no, just kidding.

0:38:54.910,0:39:01.720
Okay additional resources, full working demo iss offered here on

0:39:01.720,0:39:06.880
this link. I'm gonna be showing you because in the notebook the code stops

0:39:06.880,0:39:13.779
there. So here I just show you how you train the emulator and we got like

0:39:13.779,0:39:22.349
an MSE loss down to a very very tiny value, 0.00...

0:39:22.349,0:39:28.150
well you can read this number. Right and then this is my

0:39:28.150,0:39:35.559
value for the for the testing set, so this is going to be 38 micro MSE if

0:39:35.559,0:39:42.700
you want to call it. Here if someone wants, an extra grade maybe, you can add

0:39:42.700,0:39:50.559
the code for training the controller and it's not that trivial because we

0:39:50.559,0:39:56.829
cover how to make it work in the  class but a bit finicky. So I just show

0:39:56.829,0:40:05.200
you a final version, you can even copy from here if you want, and

0:40:05.200,0:40:13.269
if you can submit would be nice, you can get a nice reward.

0:40:13.269,0:40:18.609
So here we can start with a random position and then you can drive using the

0:40:18.609,0:40:25.720
controller, let's increase the speed, okay and boom! Another random position, okay

0:40:25.720,0:40:32.440
it's too easy. Let's make something a bit annoying, so for trailer let's say

0:40:32.440,0:40:40.720
180° and let's have this one 0°. Change angle. Okay so

0:40:40.720,0:40:48.770
this is really annoying and go see? Back and...

0:40:49.790,0:40:56.060
there we go, boom. So here you have the code, it's training in your browser, you

0:40:56.060,0:41:00.740
can go also at the bottom of this page and you have this source in GitHub, so

0:41:00.740,0:41:09.230
you can or even are encouraged to port this project here which is written

0:41:09.230,0:41:16.040
in JavaScript to PyTorch. It's going to be very a very good exercise for you to

0:41:16.040,0:41:22.850
learn. We would have actually a running notebook, which is left as

0:41:22.850,0:41:30.770
an exercise for you and you could get an additional grade I guess. Alright, so that

0:41:30.770,0:41:36.320
was it for today's class. I hope you enjoyed, let me see if there are

0:41:36.320,0:41:42.620
questions. What if we train a policy gradient? Yeah we don't know about 

0:41:42.620,0:41:45.620
reinforcement learning, I don't know anything about

0:41:45.620,0:41:52.820
reinforcement learning, sorry. [Student] I'm still confused about the architecture, can we

0:41:52.820,0:41:59.630
look at the diagram of that again? [Alfredo] Yeah, of course. So basically the

0:41:59.630,0:42:08.290
controller goes from 6 to 25 and then from 25 to 1, and they use some kind of

0:42:08.290,0:42:17.360
tanh for your activation. So 6 to 25, 25 to 1 and this is the controller.

0:42:17.360,0:42:23.270
And instead for the  trailer-truck emulator we go from 7,

0:42:23.270,0:42:32.420
which is 6: The x and y and the angle times 2 which is 6, plus 1 equal 7. So from

0:42:32.420,0:42:38.660
7 to 45 and then for from from 45 to 6. So this is my predictive model, the model

0:42:38.660,0:42:43.610
that predicts the future given the past in the actual input action. And that's

0:42:43.610,0:42:49.370
how I implemented this one here. So I have my state size which is 6, x and y and

0:42:49.370,0:42:57.080
theta times 2, and steering is 1 as it's just the angle, and we say we have 45 units,

0:42:57.080,0:43:02.780
so we have 45 units here so we go from steering size plus

0:43:02.780,0:43:07.280
state size which is 7 to this 45, then I have ReLU.

0:43:07.280,0:43:12.470
Again the it looks like they used a tanh here so okay you can write tanh here,

0:43:12.470,0:43:17.990
and then you have a linear that goes from these 45 to state size, which

0:43:17.990,0:43:23.150
is 6, which is going to be the next output here. So there is a

0:43:23.150,0:43:27.320
linear output, and again this is also something that we just put in the

0:43:27.320,0:43:30.800
midterm, I mean I'm giving you the answer of the midterm right now basically.

0:43:30.800,0:43:38.540
[Student] So where are you enforcing that the emulator actually emulates the way this

0:43:38.540,0:43:44.540
simulation works? [Alfredo] Yeah, here. So emulator training? Yeah, 

0:43:44.540,0:43:49.880
I didn't show you this one, you're right. So here I just get

0:43:49.880,0:43:53.780
the length of the training input and I get a random permutation so that I pick

0:43:53.780,0:43:59.750
at random. So I have my phi, my my angle, and the state which are going

0:43:59.750,0:44:04.280
to be the 7 coordinates is going to be picked from the ith location of these

0:44:04.280,0:44:08.930
training inputs, and these training inputs are coming down from here,

0:44:08.930,0:44:13.160
whenever I extract it. So you have training inputs, inputs are gonna be

0:44:13.160,0:44:19.190
appended to this list, which is this input list, you append the

0:44:19.190,0:44:24.170
phi, which is the steering angle, and then the initial state which comes from

0:44:24.170,0:44:29.390
the truck. So this is my input and then the output is going to be my 

0:44:29.390,0:44:37.130
output state of the of the truck. So if you go back

0:44:37.130,0:44:44.450
here you get the phi, the angle, and the state are going to be this first item of

0:44:44.450,0:44:48.830
this training input, at the location ith, the ith item of the running input,

0:44:48.830,0:44:52.130
and then you get the next state prediction which is going to be the output of

0:44:52.130,0:44:57.230
this emulator, which has a linear layer as output, right? Cool.

0:44:57.230,0:45:02.390
Then you have the next state which is going to be the output at

0:45:02.390,0:45:09.190
the ith location and now you have loss which is the criterion, which was an MSE,

0:45:09.190,0:45:15.390
criterion MSE. So you have the MSE between the next

0:45:15.390,0:45:20.130
state prediction which is this one and the next state, the true next state, then

0:45:20.130,0:45:28.230
I do basically stochastic gradient descent, I clean up the gradient... [Student] I see, so

0:45:28.230,0:45:31.110
you're basically training the emulator before you're training the rest of the

0:45:31.110,0:45:38.010
next. [Alfredo] I train the emulator only before, so we train two models: First model you

0:45:38.010,0:45:42.990
train the emulator, then whenever the emulator is trained you train the

0:45:42.990,0:45:51.540
controller which is driving the emulator, but the emulator is not longer trained. The

0:45:51.540,0:45:56.970
emulator is trained only once before, then we use the network in order to

0:45:56.970,0:46:01.890
train the controller. [Student] So you're first training the emulator and then you're

0:46:01.890,0:46:04.830
using the network you trained as emulator kind of control.

0:46:04.830,0:46:11.640
[Alfredo] Correct, yeah, so whenever I'm here, I already trained the trailer emulator.

0:46:11.640,0:46:15.990
So to train the emulator, as I show you right now the code and

0:46:15.990,0:46:20.160
then I can show you also this slide. So this was the training of

0:46:20.160,0:46:25.550
the emulator. Tthe kinematics: You have the next state given the previous state and

0:46:25.550,0:46:31.680
the angle and then you enforce this emulator to learn, to basically do a

0:46:31.680,0:46:37.320
regression and you try to copy the output. After you're done

0:46:37.320,0:46:42.180
you actually go and train the controller. To train the controller

0:46:42.180,0:46:48.090
you have this chain of blocks, which is controller and

0:46:48.090,0:46:53.940
trailer-truck network, and then you get a

0:46:53.940,0:47:00.240
trajectory, and then you enforce that the final location and the final orientation

0:47:00.240,0:47:07.590
of this trajectory, they must be the docking station and 0 for the angle,

0:47:07.590,0:47:12.540
and now you run back-propagation through this chain of things, so it's backdrop

0:47:12.540,0:47:17.790
through time in order to adapt, they use the term 'adapt' in this paper,

0:47:17.790,0:47:25.050
the weights of the controller such that it manages to map the original initial

0:47:25.050,0:47:29.930
random position to this final target position

0:47:29.930,0:47:34.820
and orientation configuration, let's call it configuration. So we start with a

0:47:34.820,0:47:41.030
random initial configuration which is corresponding to position and

0:47:41.030,0:47:47.270
angles, and then you enforce that the final output of this sequence

0:47:47.270,0:47:53.990
of modules is going to be giving you the the docking station and 0 on the

0:47:53.990,0:48:01.790
backside of the truck. So this is two parts: Training first the

0:48:01.790,0:48:08.180
emulator, finish that, then you train the controller in order to 

0:48:08.180,0:48:13.670
actually reach a specific goal. The number of red boxes here varies and

0:48:13.670,0:48:19.550
it depends on every episode because you don't know how many steps are goning be

0:48:19.550,0:48:27.680
required for you to reach destination given initial condition. So

0:48:27.680,0:48:34.730
many words I said, oh my God, does it make sense? [Student] Yes. [Alfredo] OK, very good.

0:48:34.730,0:48:41.810
Next question. [Student] Somebody did ask this, why we needed to train the

0:48:41.810,0:48:48.680
emulator instead of just using the model. [Alfredo] Yeah, the answer was that not

0:48:48.680,0:48:55.510
every time you actually have the questions of the

0:48:55.510,0:49:01.430
kinematics, so let's say, and this is going to be coming up next lesson I

0:49:01.430,0:49:04.910
think whenever I'm going to be talking about my own research. I'd like to figure

0:49:04.910,0:49:10.370
out what is the behavior of other cars when you drive in a highway, but I can't

0:49:10.370,0:49:15.740
control other cars, I have no idea how what is the behavior of other cars,

0:49:15.740,0:49:20.180
so the only way I can learn how other cars react to my actions is actually

0:49:20.180,0:49:25.190
through observations and therefore we we have some

0:49:25.190,0:49:29.900
cameras mounted on a 30-story building looking at the highway

0:49:29.900,0:49:35.170
section and then you basically figure out what is the

0:49:35.170,0:49:39.290
interaction between vehicles, and therefore we had to learn these forward models

0:49:39.290,0:49:42.650
called predictive model, which is figuring out what is going to

0:49:42.650,0:49:49.130
be the reaction of other vehicles given your own actions. So in this case, 

0:49:49.130,0:49:56.030
you don't need the emulator but they train these emulators such that it's

0:49:56.030,0:50:02.180
more generic, you don't need to have differentiable equations. [Student] I see,

0:50:02.180,0:50:08.890
okay. One one more question, so when you said the length of this recurrent

0:50:08.890,0:50:14.540
network will be variable, there was something about having it be like four

0:50:14.540,0:50:23.330
times the length of the number of steps or something like that, could you go into

0:50:23.330,0:50:27.980
that a bit more? [Alfredo] Yes, so here we assume that each length of

0:50:27.980,0:50:35.090
each episode is capital K, so the lowercase k is the actual

0:50:35.090,0:50:40.760
index, where you go like 0, 1, 2, 3, 4, 5,  whatever, so each episode

0:50:40.760,0:50:47.150
has whatever capital K number of steps. So capital K is going to

0:50:47.150,0:50:56.390
be different for every episode. So each of these two items here, this guy

0:50:56.390,0:51:00.740
here has two affine transformations and this guy here has two affine

0:51:00.740,0:51:04.370
transformations, so overall the network that you are

0:51:04.370,0:51:11.260
seeing here has four affine transformations times capital K.

0:51:11.270,0:51:18.160
[Student] Oh I se, okay. [Alfredo] That's basically one  neural net, right? So it's a neural net which is

0:51:18.160,0:51:22.850
not even a recurrent neural net, it's just a feed-forward neural net

0:51:22.850,0:51:29.780
with four times capital K number of affine transformations. And now you train

0:51:29.780,0:51:34.400
with back prop in order to enforce always the same target, so that's

0:51:34.400,0:51:40.190
actually funny to see in this way. So you have a neural network which label or

0:51:40.190,0:51:45.800
target is going to be always the same, but then the network can change lengths

0:51:45.800,0:51:50.810
and the input can be different. So you had you have a network, 

0:51:50.810,0:51:56.090
you input different things, you can change the length, the height,

0:51:56.090,0:52:00.890
the depth of the network but you always have the same target here. So

0:52:00.890,0:52:05.510
usually when you do regression or classification we have a fixed network,

0:52:05.510,0:52:10.850
you input different inputs like here and then you have different targets on here,

0:52:10.850,0:52:16.760
target or classes if you're doing classification or labels. In

0:52:16.760,0:52:23.359
this case, you have different inputs, the target is always fixed and you have you

0:52:23.359,0:52:31.040
know different lengths; so you train a network, a variable depth network with

0:52:31.040,0:52:36.800
variable inputs and a fixed target. How cool is that?

0:52:36.800,0:52:42.590
[Student] Do we enforce like a maximum length... [Alfredo] yeah, of course,

0:52:42.590,0:52:49.280
otherwise you can wooo... Do we need an emulator to train the neural net

0:52:49.280,0:52:53.750
emulator? Is the point of having a neural net emulator to have a differentiable...

0:52:53.750,0:52:56.810
Yeah that's the point, the whole point is to have a differentiable

0:52:56.810,0:53:04.310
emulator, which is not always the case, in case of you just have

0:53:04.310,0:53:08.990
observations then you don't have gradients, you just have observations. And

0:53:08.990,0:53:12.410
you want to learn a network that allows you to tell you what is gonna be the

0:53:12.410,0:53:18.900
Jacobian as you go back. More questions? [Student] I have a question more

0:53:18.900,0:53:24.600
related to just like implementation, it seems like for training the

0:53:24.600,0:53:30.630
controller we freeze the weights for t but we still need to pass the

0:53:30.630,0:53:35.570
gradients through in order to update freely each of the cells, is that right? So I

0:53:35.570,0:53:39.870
guess, would we then when we define our optimizer we're just essentially

0:53:39.870,0:53:45.450
just feeding it the controller parameters, but when we called the

0:53:45.450,0:53:49.160
backwards it's all still connected to the same network?

0:53:49.160,0:54:00.180
[Alfredo] So this is gonna be exactly, PyTtorch examples, what we have seen

0:54:00.180,0:54:15.510
last week when we were going through the DC GAN, so you have an optimizer...

0:54:15.510,0:54:24.000
hold on, where is it, you're gonna have an optimizer from the one network 

0:54:24.000,0:54:27.930
and I have an optimizer for the other network, that's it, whenever you have the training

0:54:27.930,0:54:31.830
you actually have two distinct training, in this case when you train a generative

0:54:31.830,0:54:36.930
adversarial network you have both networks stepping in the same loop but

0:54:36.930,0:54:40.920
you can have one training thing first, you start with the first network,

0:54:40.920,0:54:45.630
then later below you're gonna have the other 

0:54:45.630,0:54:49.830
network step in there. So you had two optimizers which are

0:54:49.830,0:54:53.730
'adapting', if you use this word there from this paper, the weights at

0:54:53.730,0:54:58.050
different time. It's actually two different networks which don't even

0:54:58.050,0:55:01.860
train at the same time. So you first train the predictive model, the forward

0:55:01.860,0:55:07.520
model. Whenever you finish that you use that as a mean to send back

0:55:07.520,0:55:12.810
gradients from the future. How do we choose capital K?

0:55:12.810,0:55:18.140
Capital K is the number of iterations that are necessary in order for you to

0:55:18.140,0:55:25.560
reach any edge, you just go back until you hit something. Whenever you hit

0:55:25.560,0:55:32.310
something, that's capital K. So actually whenever we drive forward we

0:55:32.310,0:55:36.900
use the kinematic model such that you have a truthful final

0:55:36.900,0:55:40.410
location, but then in order to run the gradients backwards you're going to be

0:55:40.410,0:55:45.510
using the emulator network. So you use the kinematics model to do the forward

0:55:45.510,0:55:50.420
pass and you do the backward pass through using the emulator network. I

0:55:50.420,0:55:54.960
think this can be done better with policy gradient and deep RL model.

0:55:54.960,0:56:00.780
Okay we don't know about RL, RL for us doesn't make sense. I'm

0:56:00.780,0:56:06.240
just repeating what the boss says. You can try, you can definitely try out

0:56:06.240,0:56:10.320
and see whether it works. Again, this stuff was done in the 90's, so

0:56:10.320,0:56:20.370
that's old stuff but it's is always you know, how do you call it, 'pertinent'

0:56:20.370,0:56:30.270
there you go. More questions? [Student] Hi Alfredo I'm still confused about training for controller and

0:56:30.270,0:56:36.090
emulator. So the emulator is trained at each time step because we are

0:56:36.090,0:56:42.720
comparing the predicted state versus the truth... [Alfredo] This one, right? 

0:56:42.720,0:56:48.960
[Student] Yeah, each time step, so we are updating the parameters for every time step?

0:56:48.960,0:56:53.760
[Alfredo] Well you can also do a batch if you want but you can do stochastic gradient,

0:56:53.760,0:56:56.610
this is okay, so you can provide a new sample

0:56:56.610,0:57:00.330
and then you update your sample update and so on. Or you can actually 

0:57:00.330,0:57:06.980
step after several  time steps. [Student] Okay and when we hit

0:57:06.980,0:57:12.720
the big K, we just... [Alfredo] This is not about the emulator, there is no capital K

0:57:12.720,0:57:20.010
here. [Student] Oh. I'm confused because we do the training for

0:57:20.010,0:57:25.200
emulator first and then when we hit the terminate state we then do backdrop

0:57:25.200,0:57:33.780
for controller. [Alfredo] So first you train this network. Finished. Done. Second step: You

0:57:33.780,0:57:37.680
train the controller, next network.  Alright so you train first the first

0:57:37.680,0:57:41.519
network, this one with random numbers, with random steering signal,

0:57:41.519,0:57:47.069
there is no controller here, right? [Student] Yeah. [Alfredo] Okay, cool. So you first

0:57:47.069,0:57:53.549
trained this emulator such that it can replicate these dynamics. [Student] Okay.

0:57:53.549,0:57:57.869
[Alfredo] Then, second part is gonna be training the controller, and the controller is trained

0:57:57.869,0:58:04.559
in this manner: You provide initial condition, you feed-forward this initial

0:58:04.559,0:58:08.909
condition, you basically end up with a trajectory of 'h' case

0:58:08.909,0:58:15.839
until you reach one of the three final conditions, which are:

0:58:15.839,0:58:20.399
Jackknifing, running out of steps or you actually hit a wall.

0:58:20.399,0:58:25.439
If you hit a wall then you run  back-propagation through this network and

0:58:25.439,0:58:29.999
then you do gradient descent. [Student] And now you're doing gradient descent

0:58:29.999,0:58:36.269
with regards to the controller. [Alfredo] Only C yes, yes, yes. [Student] Okay, okay, yeah I got it,

0:58:36.269,0:58:43.949
thank you. [Alfredo] Okay, that's awesome. That's it, I think.

0:58:43.949,0:58:48.449
And so you made it until the end of the lesson. Congratulations. So how can you

0:58:48.449,0:58:53.130
better get an understanding of what we cover today? So there are a few things

0:58:53.130,0:58:59.099
you can do to keep going. Comprehension: You have some questions?

0:58:59.099,0:59:04.319
ask them just in the comment section below, we'll answer every one. News: If you

0:59:04.319,0:59:08.819
follow me on Twitter under @alfcnz, you can get the latest information as I

0:59:08.819,0:59:13.409
post them online. Updates: If you subscribe to the channel and turn on the

0:59:13.409,0:59:17.989
notification button you will not lose any of the videos I'm posting here.

0:59:17.989,0:59:22.229
Appreciation: Again, if you like this video and the content and everything I

0:59:22.229,0:59:27.839
do, I would really appreciate if you put a like on the video. Searching:

0:59:27.839,0:59:32.159
Every video has an English transcription which can be searchable and you

0:59:32.159,0:59:35.029
can find it in the video description below.

0:59:35.029,0:59:40.439 
Language: Sei parla italiano? hablas español? 你会说中文吗? Do you speak Korean?

0:59:40.439,0:59:44.369
Turkish, we have now! All these translations are now available for you.

0:59:44.369,0:59:51.569
I'm planning to add more languages as we have volunteers. PyTorch: If you'd like

0:59:51.569,0:59:56.730
to have a concrete understanding and digest better this topic, I highly

0:59:56.730,1:00:01.830
recommend to you to try to train the controller yourself, and if he works you

1:00:01.830,1:00:07.440
can submit a pull request and that's actually the next point,

1:00:07.440,1:00:11.790
(Contribute) such that we're gonna have now a notebook which will have a running

1:00:11.790,1:00:16.800
controller, so this is left to you as an exercise such that you can

1:00:16.800,1:00:22.350
actually master this topic. Alright, thank you again for listening, see you
