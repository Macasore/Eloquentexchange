"use client";

import { Button } from "@/components/ui/button";
import { Data } from "iconsax-react";
import { useTheme } from "next-themes";
import Image from "next/image";
<<<<<<< HEAD
import { useRouter } from "next/navigation";

const ReferralSection = () => {
  const { resolvedTheme } = useTheme();
  const router = useRouter();
=======

const ReferralSection = () => {
  const { resolvedTheme } = useTheme();
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
  return (
    <div className="flex flex-col space-y-10 px-10 pt-5">
      <div className="flex min-[912px]:flex-row flex-col justify-between items-center">
        <div className="flex flex-col min-[912px]:items-start items-center space-y-6">
          <Image
<<<<<<< HEAD
<<<<<<< HEAD
            src={
              resolvedTheme === "dark" ? "/logo-and-text.png" : "eloq-light.svg"
            }
            alt="text-and-logo"
            width={350}
            height={350}
            className="max-[912px]:hidden block"
          />
          <Image
            src={
              resolvedTheme === "dark" ? "/logo-and-text.png" : "eloq-light.svg"
            }
            alt="text-and-logo"
            width={200}
            height={200}
            className="min-[912px]:hidden block"
=======
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            src="/logo-and-text.png"
            alt="text-and-logo"
            width={350}
            height={350}
<<<<<<< HEAD
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
          />
          <h3 className="font-medium min-[912px]:text-5xl text-2xl min-[912px]:text-left text-center leading-normal">
            <span className="text-[#4168B7] dark:text-[#A77700]">Refer</span>{" "}
            and earn big <br /> rewards
          </h3>
          <Image
<<<<<<< HEAD
<<<<<<< HEAD
            src={resolvedTheme === "dark" ? "/referral.png" : "referimg.svg"}
=======
            src="/referral.png"
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
            src="/referral.png"
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            alt="referral"
            width={200}
            height={200}
            className="min-[912px]:hidden block"
          />
          <p className="font-normal min-[912px]:text-xl text-sm min-[912px]:text-left text-center text-primary w-3/5">
            Referrals is a powerful way to strengthen and expand our network and
            a wonderful way for you to earn rewards.
          </p>
          <div>
            <Button
              variant="custom"
              className="rounded-br-none rounded-tl-none rounded-tr-lg rounded-bl-lg"
<<<<<<< HEAD
              onClick={() => router.push("/refer&earn")}
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            >
              Refer Now <Data className="ml-2 w-4 h-4" />
            </Button>
          </div>
        </div>
        <Image
<<<<<<< HEAD
<<<<<<< HEAD
          src={resolvedTheme === "dark" ? "/referral.png" : "referimg.svg"}
=======
          src="/referral.png"
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
          src="/referral.png"
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
          alt="referral"
          width={500}
          height={500}
          className="min-[912px]:block hidden"
        />
      </div>
      <div className="flex justify-center">
        <Image
          src={resolvedTheme === "dark" ? "/roadmap-dark.png" : "/roadmap.png"}
          alt="roadmap"
          width={500}
          height={500}
        />
      </div>
      <div className="flex flex-col space-y-1">
        <div className="flex min-[912px]:flex-row flex-col min-[912px]:space-y-0 space-y-10 justify-between items-center">
<<<<<<< HEAD
          <h3 className="min-[912px]:text-5xl mb-2 pb-1 text-xl min-[912px]:text-left text-center font-medium leading-normal">
=======
          <h3 className="min-[912px]:text-5xl text-xl min-[912px]:text-left text-center font-medium leading-normal">
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            Here are some{" "}
            <span className="text-[#4168B7] dark:text-[#A77700]">
              acceptable
            </span>{" "}
<<<<<<< HEAD
            <br className="min-[912px]:block hidden" />
            <span> payment method on </span>
            <br className="min-[912px]:block hidden" />{" "}
            <p className="text-[#4168B7] mt-2 pt-1 dark:text-[#A77700]">
              Eloquent Exchange.
            </p>
          </h3>
          <Image
<<<<<<< HEAD
            src={
              resolvedTheme === "dark"
                ? "/credit_card_dark.png"
                : "referimg2.svg"
            }
=======
            src="/credit_card_dark.png"
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
            <br className="min-[912px]:block hidden" /> payment method on{" "}
            <br className="min-[912px]:block hidden" />{" "}
            <span className="text-[#4168B7] dark:text-[#A77700]">
              Eloquent Exchange.
            </span>
          </h3>
          <Image
            src="/credit_card_dark.png"
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            alt="credit_card_payment"
            width={500}
            height={500}
          />
        </div>
        <div className="flex justify-center items-center">
          <Image
<<<<<<< HEAD
<<<<<<< HEAD
            src="/demo_light.svg"
=======
            src="/demo_card_dark.svg"
>>>>>>> 8fd29388e9d31c807186c0f278798cbae48e893c
=======
            src="/demo_card_dark.svg"
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
            alt="demo_card"
            width={600}
            height={600}
          />
        </div>
      </div>
    </div>
  );
};

export default ReferralSection;
