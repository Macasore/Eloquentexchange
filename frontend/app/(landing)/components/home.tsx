"use client";

import React from "react";
import { Button } from "@/components/ui/button";
import Image from "next/image";
import TypewriterComponent from "typewriter-effect";
import { Bitcoin, Chart, Courthouse, UserOctagon } from "iconsax-react";
import { Revalia } from "next/font/google";
import { cn } from "@/lib/utils";
import { useTheme } from "next-themes";
import { companies } from "./companies";
<<<<<<< HEAD
import { useRouter } from "next/navigation";
<<<<<<< HEAD
// import Ticker from "react-ticker";
// import Ticker from "react-awesome-ticker";
// import Marquee from "react-double-marquee";
=======
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c

const font = Revalia({
  subsets: ["latin"],
  weight: ["400"],
});

const HomeSection = () => {
  const { resolvedTheme } = useTheme();
<<<<<<< HEAD
  const router = useRouter();
  return (
    <div id="home" className="flex flex-col space-y-8 px-10 pt-10">
      <div className="flex min-[912px]:flex-row md:my-4 flex-col min-[912px]:text-left text-center justify-between items-center">
<<<<<<< HEAD
        <div className="flex flex-col md:my-4 md:mt-4 my-2 gap-y-6">
          <h3 className="font-medium space-y-3 my-auto mb-4  text-primary text-3xl my-3 sm:text-3xl md:text-6xl leading-snug">
=======
  return (
    <div id="home" className="flex flex-col space-y-8 px-10 pt-10">
      <div className="flex min-[912px]:flex-row flex-col min-[912px]:text-left text-center justify-between items-center">
        <div className="flex flex-col gap-y-6">
          <h3 className="font-medium text-primary text-3xl leading-snug">
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            <TypewriterComponent
              options={{
                strings: [
                  "Start trading in crypto in an",
                  "Enjoy the best market rates with",
                  "Instant Trades: Secure Your",
<<<<<<< HEAD
=======
        <div className="flex flex-col my-2 gap-y-6">
          <h3 className="font-medium text-primary text-3xl my-3 sm:text-3xl md:text-6xl leading-snug">
            <TypewriterComponent
              className="space-y-3 my-auto mb-3"
              options={{
                strings: [
                  "Start trading in crypto in an \n instant.",
                  "Enjoy the best market rates with \n Eloquent Exchange.",
                  "Instant Trades: Secure Your \n Investments!",
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
                ],
                autoStart: true,
                loop: true,
                delay: 100,
<<<<<<< HEAD
                deleteSpeed: 100,
              }}
            />
<<<<<<< HEAD
            <span className="text-[#4168B7] mt-3 mb-2 dark:text-[#A77700]">
              <TypewriterComponent
=======
            <span className="text-[#4168B7] dark:text-[#A77700]">
              {/* <TypewriterComponent
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
                deleteSpeed: 150,
              }}
            />
            <span className="text-[#4168B7] dark:text-[#A77700]">
              <TypewriterComponent
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
                options={{
                  strings: ["instant.", "Eloquent Exchange.", "Investments !"],
                  autoStart: true,
                  loop: true,
                  delay: 200,
<<<<<<< HEAD
                  deleteSpeed: 500,
                }}
<<<<<<< HEAD
              />
=======
              /> */}
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
                  deleteSpeed: 300,
                }}
              />
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            </span>
          </h3>
          <div className="flex min-[912px]:hidden min-[912px]:justify-start justify-center">
            <Image
<<<<<<< HEAD
<<<<<<< HEAD
              src={resolvedTheme === "dark" ? "/homes-dark.svg" : "/homes.svg"}
              width={300}
              height={300}
              alt="Image"
              className="object-cover min-[912px]:hidden object-center"
            />
          </div>
          <p className="text-primary w-3/4 font-normal min-[912px]:text-2xl text-sm">
=======
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
              src={resolvedTheme === "dark" ? "/home-dark.svg" : "/home.svg"}
              width={300}
              height={300}
              alt="Image"
              className="object-cover object-center"
            />
          </div>
          <p className="text-primary font-normal min-[912px]:text-2xl text-sm">
<<<<<<< HEAD
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            Join the world&apos;s biggest and trusted exchange. Trade in
            Bitcoin, Etherum, dodge and many more currencies.
          </p>
          <div>
            <Button
              variant="custom"
              className="rounded-br-none rounded-tl-none rounded-tr-lg rounded-bl-lg"
<<<<<<< HEAD
              onClick={() => router.push("/dashboard/transactions/buy&sell/")}
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            >
              Trade Crypto
              <Bitcoin className="h-6 w-6 ml-2 rotate-45" />
            </Button>
          </div>
        </div>
        <Image
<<<<<<< HEAD
<<<<<<< HEAD
          src={resolvedTheme === "dark" ? "/homes-dark.svg" : "/homes.svg"}
          width={500}
          height={500}
=======
          src={resolvedTheme === "dark" ? "/home-dark.svg" : "/home.svg"}
          width={300}
          height={300}
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
          src={resolvedTheme === "dark" ? "/home-dark.svg" : "/home.svg"}
          width={300}
          height={300}
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
          alt="Image"
          className="object-cover object-center min-[912px]:flex hidden"
        />
      </div>
      <div
        className={cn(
          "text-center text-primary min-[912px]:block hidden",
          font.className
        )}
      >
<<<<<<< HEAD
<<<<<<< HEAD
        {/* <Ticker>This is the Headline of element</Ticker> */}
        {/* <Marquee>Some really really really really really long text</Marquee> */}
        <div className="marquee">
          <p className="text-black dark:text-white">
            {" "}
            Welcome to Eloquent Exchange. Your one stop community for all
            cryptocurrencies 🚀.
          </p>
        </div>

        {/* <div className="text-xl">
          <marque>
            Welcome to Eloquent Exchange. Your one stop community for all
            cryptocurrencies 🚀.
          </marque>
        </div> */}
=======
        <marquee className={cn("text-xl")}>
          Welcome to Eloquent Exchange. Your one stop community for all
          cryptocurrencies 🚀."
        </marquee>
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
        {/* <TypewriterComponent
=======
        <TypewriterComponent
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
          options={{
            strings:
              "Welcome to Eloquent Exchange. Your one stop community for all cryptocurrencies 🚀.",
            autoStart: true,
            loop: true,
          }}
<<<<<<< HEAD
        /> */}
=======
        />
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
      </div>
      <div className="flex space-x-12 justify-center items-center">
        {companies.map((company) => (
          <Image
            key={company.src}
            src={company.src}
            alt={company.alt}
            className={company.className}
            width={100}
            height={100}
          />
        ))}
      </div>
      <div className="flex flex-col space-y-8 pt-20">
        <div className="flex min-[912px]:flex-row flex-col min-[912px]:text-left text-center justify-between space-y-8 min-[912px]:space-y-0">
          <div className="flex flex-col space-y-8">
<<<<<<< HEAD
            <h2 className="min-[912px]:font-semibold min-[912px]:text-5xl text-3xl font-normal">
              Start Trading with Eloquent <br />{" "}
              <p className="mt-1">
                <span className="text-[#4168B7] dark:text-[#A77700]">
                  {" "}
                  Exchange
                </span>{" "}
                in a few steps.
              </p>
            </h2>
=======
            <h3 className="min-[912px]:font-semibold text-2xl font-normal">
              Start Trading with Eloquent <br /> Exchange in a few steps
            </h3>
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            <div>
              <Button
                variant="custom"
                className="rounded-br-none rounded-tl-none rounded-tr-lg rounded-bl-lg"
<<<<<<< HEAD
                onClick={() => router.push("/dashboard/transactions/buy&sell/")}
=======
                disabled
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
              >
                Trade Crypto <Bitcoin className="h-6 w-6 ml-2 rotate-45" />
              </Button>
            </div>
          </div>
          {/* <Image
            src="/rocket-straight.svg"
            width={100}
            height={100}
            alt="rocket"
            className="object-cover object-center"
          /> */}
          <div className="flex min-[912px]:justify-start justify-center items-center">
            <div className="flex w-[380px] p-8 items-center border border-primary rounded-br-none rounded-tl-none rounded-tr-2xl rounded-bl-2xl">
              <UserOctagon className="h-10 w-10 mr-4" />
              <div className="flex flex-col space-y-2 text-primary text-left">
                <h2 className="font-semibold text-lg">Create Account</h2>
                <p className="font-normal text-sm">
                  Sign up with your{" "}
                  <span className="text-[#4168B7] dark:text-[#A77700]">
                    email
                  </span>{" "}
                  within <br /> minutes, and{" "}
                  <span className="text-[#4168B7] dark:text-[#A77700]">
                    verify identity.
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
        <div className="flex items-center justify-center">
          <div className="flex w-[380px] p-8 items-center border border-primary rounded-br-none rounded-tl-none rounded-tr-2xl rounded-bl-2xl">
            <Courthouse className="h-10 w-10 mr-4" />
            <div className="flex flex-col space-y-2 text-primary">
              <h2 className="font-semibold text-lg">Verify payment mode</h2>
              <p className="font-normal text-sm">
                Verify your mode of{" "}
                <span className="text-[#4168B7] dark:text-[#A77700]">
                  payment
                </span>{" "}
                in an <br /> easy way.
              </p>
            </div>
          </div>
        </div>
        <div className="flex min-[912px]:justify-start justify-center items-center">
          <div className="flex w-[380px] p-8 items-center border border-primary rounded-br-none rounded-tl-none rounded-tr-2xl rounded-bl-2xl">
            <Chart className="h-10 w-10 mr-4" />
            <div className="flex flex-col space-y-2 text-primary">
              <h2 className="font-semibold text-lg">Start trading instantly</h2>
              <p className="font-normal text-sm">
                <span className="text-[#4168B7] dark:text-[#A77700]">
                  Buy & sell
                </span>{" "}
                variety of top coins at <br /> the best prices.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomeSection;
